import torch
import numpy as np
import matplotlib.pyplot as plt
import os

# parameters

# D_in = 1
H = 10
D_out = 5
learning_rate = 1e-2

number_of_players = 100

D_in = (number_of_players * number_of_players * 2 + 2)
brain_a = torch.nn.Sequential(
                  torch.nn.Linear(D_in, H),
                  torch.nn.Sigmoid(),
                  torch.nn.Linear(H, D_out),
                  torch.nn.Sigmoid()
              )
brain_b = torch.nn.Sequential(
                  torch.nn.Linear(D_in, H),
                  torch.nn.Sigmoid(),
                  torch.nn.Linear(H, D_out),
                  torch.nn.Sigmoid()
              )
optimizer_a = torch.optim.Adam(brain_a.parameters(), lr=learning_rate)
optimizer_b = torch.optim.Adam(brain_b.parameters(), lr=learning_rate)
loss_fn = torch.nn.MSELoss(reduction='sum')
class Player:

  playersid = 0
  players = []
  positions = dict()
  def __init__(self, team, row, col, number_of_players):
    self.number_of_players = number_of_players
    self.id = Player.playersid
    Player.playersid += 1
    self.row = row
    self.col = col
    self.position = str(row) + ' ' + str(col)
    if self.position in Player.positions.keys():
      Player.positions[self.position][self.id] = self
    else:
      Player.positions[self.position] = {self.id: self}

    self.team = team
    self.score = 0
    self.last_move = None
    Player.players.append(self)

  def die(self):
    self.alive = False
    if len(Player.positions[self.position]) == 1:
      del Player.positions[self.position]
    else:
      del Player.positions[self.position][self.id]

  def move(self, state):
    state = torch.Tensor(state)
    if self.team == 'a':
      self.last_move = brain_a(state)
    else:
      self.last_move = brain_b(state)
    self.last_max = np.argmax(self.last_move.detach().numpy())

    if len(Player.positions[self.position]) == 1:
      del Player.positions[self.position]
    else:
      del Player.positions[self.position][self.id]

    # if self.last_max == 0:
      #  print("standing")

    if self.last_max == 1: # move left
      self.col -= 1
      if self.col < 0:
        self.col = self.number_of_players - 1

    if self.last_max == 2: # move forward
      self.row += 1
      if self.row > self.number_of_players - 1:
        self.row = 0

    if self.last_max == 3: # move right
      self.col += 1
      if self.col > self.number_of_players - 1:
          self.col = 0

    if self.last_max == 4: # move backwards
      self.row -= 1
      if self.row < 0:
        self.row = self.number_of_players - 1
    self.position = str(self.row) + ' ' + str(self.col)

    if self.position in Player.positions.keys():
      Player.positions[self.position][self.id] = self
    else:
      Player.positions[self.position] = {self.id: self}

    return self.row, self.col

  def reward(self, r):
    R = np.zeros(D_out)
    R[self.last_max] = r
    loss = loss_fn(self.last_move, torch.Tensor(R))
    if self.team == 'a':
      optimizer_a.zero_grad()
      loss.backward()
      optimizer_a.step()
    else:
      optimizer_b.zero_grad()
      loss.backward()
      optimizer_b.step()

  def __str__(self):
    return 'id:' + str(self.id) + '|team:' + self.team + '|score:' + str(self.score) + '|row:' + str(self.row) + '|col:'+ str(self.col)
  
  def __repr__(self):
    return 'id:' + str(self.id) + '|team:' + self.team + '|score:' + str(self.score) + '|row:' + str(self.row) + '|col:'+ str(self.col)



class World:
  def __init__(self, number_of_players):
    self.number_of_players = number_of_players
    team_a = [Player('a', 0, col, number_of_players) for col in range(number_of_players)]
    team_b = [Player('b', number_of_players - 1, col, number_of_players) for col in range(number_of_players)]

  def plot(self):
    plt.xlim((-1, self.number_of_players))
    plt.ylim((-1, self.number_of_players))
    for player in Player.players:
      if player.team == 'a':
        plt.plot(player.row, player.col, 'r.')
      else:
        plt.plot(player.row, player.col, 'bx')
    # plt.show()

  def move_all(self):
    state = np.zeros((self.number_of_players, self.number_of_players, 2))
    for player in Player.players:
      if player.team == 'a':
        state[player.row, player.col, 0] += 1 / self.number_of_players
      else:
        state[player.row, player.col, 1] += 1 / self.number_of_players
    state = state.flatten()

    for player in Player.players:
      player.move(np.append(state, [player.row / self.number_of_players, player.col / self.number_of_players]))
      
    # print(Player.positions,'\n')

  def reward_all(self):
    for di in Player.positions.values():
      if len(di) > 1:
        a = []
        b = []
        has_a_player = False
        has_b_player = False
        for player in di.values():
          if player.team == 'a':
            a.append(player)
            has_a_player = True
          else:
            b.append(player)
            has_b_player = True
        if has_a_player and has_b_player:
          if len(a) > len(b):
            for player in a:
              player.reward(1)
              player.score += 1
            for player in b:
              player.reward(-1)
              player.score -= 1
          if len(a) < len(b):
            for player in a:
              player.reward(-1)
              player.score -= 1
            for player in b:
              player.reward(1)
              player.score += 1




  # def remove(self, player)


w = World(100)

path = "images_single/"
os.makedirs(path, exist_ok=True)

for i in range(200):
  w.move_all()
  w.reward_all()
  w.plot()
  plt.savefig('images_single/' + str(i) + '.png')
  plt.close()



for p in Player.players:
  print(p)

'''
p1 = Player(0, 0, 0)
p2 = Player(0, 1, 0)

for _ in range(100):
  p1.move(torch.Tensor([10]))
  p1.reward(torch.Tensor(1))

  p2.move(torch.Tensor([10]))
  p2.reward(torch.Tensor(1))
'''