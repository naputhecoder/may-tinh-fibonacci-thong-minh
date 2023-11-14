def my_rfibo(n):
  if n == 0:
    return 0
  elif n == 1: 
    return 1
  else:
    return my_rfibo(n-1) + my_rfibo(n-2)

a = input('Nhap con so may man: ')
a = int(a)
print(my_rfibo(a))