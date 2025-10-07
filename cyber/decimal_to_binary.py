def decimal_to_binary(num,bits):
  if num>=0:
    return format(num,f'0{bits}b')
  else:
    return format((1<<bits)+num,f'0{bits}b')

num= int(input("enter your num you want to convert - "))
bits= int(input("enter your num of bits - "))
print(decimal_to_binary(num,bits))
