import torch
import numpy as np
import matplotlib.pyplot as plt
import os

H = 100
D_out = 2
Lr = 0.0001

# R11,R12 | R21,R12 
# R21,R22 | R21,R22 

P1 = torch.nn.Sequential(
          torch.nn.Linear(1, H),
          torch.nn.Sigmoid(),

          torch.nn.Linear(H, H),
          torch.nn.Sigmoid(),

          torch.nn.Linear(H, D_out),
          torch.nn.Sigmoid()
      )

optimizer_P1 = torch.optim.Adagrad(P1.parameters())


P2 = torch.nn.Sequential(
          torch.nn.Linear(1, H),
          torch.nn.Sigmoid(),

          torch.nn.Linear(H, H),
          torch.nn.Sigmoid(),

          torch.nn.Linear(H, D_out),
          torch.nn.Sigmoid()
      )

optimizer_P2 = torch.optim.Adagrad(P2.parameters())

criterion = torch.nn.MSELoss()


for step in range(10000):  # choice[0] > choice[1] --> silent
  P1_choice = P1(torch.Tensor([1]))
  P2_choice = P2(torch.Tensor([1]))
  # print(P1_choice)
  # print(P2_choice)
  # print('\n')

  if P1_choice[0] > P1_choice[1] and P2_choice[0] > P2_choice[1]:
    if step % 100 == 0: print('both soccer')
    target_P1 = P1_choice.clone()
    target_P1[0] = 10
    target_P2 = P2_choice.clone()
    target_P2[0] = 1
    loss_P1 = criterion(P1_choice, target_P1)
    loss_P2 = criterion(P2_choice, target_P2)

  if P1_choice[0] < P1_choice[1] and P2_choice[0] < P2_choice[1]:
    if step % 100 == 0: print('both concert')
    target_P1 = P1_choice.clone()
    target_P1[1] = 1
    target_P2 = P2_choice.clone()
    target_P2[1] = 10
    loss_P1 = criterion(P1_choice, target_P1)
    loss_P2 = criterion(P2_choice, target_P2)

  if P1_choice[0] > P1_choice[1] and P2_choice[0] < P2_choice[1]:
    if step % 100 == 0: print('P1 soccer | P2 concert')
    target_P1 = P1_choice.clone()
    target_P1[0] = 0
    target_P2 = P2_choice.clone()
    target_P2[1] = 0
    loss_P1 = criterion(P1_choice, target_P1)
    loss_P2 = criterion(P2_choice, target_P2)

  if P1_choice[0] < P1_choice[1] and P2_choice[0] > P2_choice[1]:
    if step % 100 == 0: print('P1 concert | P2 soccer')
    target_P1 = P1_choice.clone()
    target_P1[1] = 0
    target_P2 = P2_choice.clone()
    target_P2[0] = 0
    loss_P1 = criterion(P1_choice, target_P1)
    loss_P2 = criterion(P2_choice, target_P2)


  optimizer_P1.zero_grad()
  optimizer_P2.zero_grad()
  loss_P1.backward()
  loss_P2.backward()
  optimizer_P1.step()
  optimizer_P2.step()
