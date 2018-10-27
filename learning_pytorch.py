import torch
import numpy as np









x = torch.autograd.Variable(torch.ones(2,2), requires_grad=True)
print(x.grad)

# y = x + 3
y = torch.autograd.Variable(torch.Tensor([1]), requires_grad=True)
print(y)
y.backward()



print(x.grad)





exit()
batch_size = 100





linear = torch.nn.Linear(2, 1)

criterion = torch.nn.MSELoss()
optimizer = torch.optim.SGD(linear.parameters(), lr=0.0001)


for step in range(100000):
  x = torch.randn(batch_size, 2)
  # print('x:', x)
  y = torch.sum(x, 1).view(-1,1)
  pred = linear(x)


  # print('y:', y)
  # print('p:', pred)
  # Compute loss.
  loss = criterion(pred, y)
  if step % 100 == 0:
    print('loss: ', loss)

  # Backward pass.
  optimizer.zero_grad()
  loss.backward()
  optimizer.step()

