num=int(input("enter num for make it binary: "))
numofbites=int(input("enter num of bites"))
binaric_num=""
if num>=0:
  while numofbites>0:
    if 2**(numofbites-1)<=num :
     binaric_num+="1"
     num-=2**(numofbites-1)
    else:
      binaric_num+="0"
    numofbites=numofbites-1
else:
   bits=numofbites
   absnum=abs(num)
   while numofbites>0:
      if 2**(numofbites-1)<=absnum :
       binaric_num+="0"
       absnum-=2**(numofbites-1)
      else:
        binaric_num+="1"
      numofbites=numofbites-1
      binaric_num = bin(int(binaric_num, 2) + 1)[2:].zfill(bits)
print(binaric_num)
