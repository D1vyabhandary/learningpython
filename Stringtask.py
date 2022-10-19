#1.find the length of string without using length function ?

# l="python is programing language"
# count=0
# for i in l:
#     count=count+1
# print(count)

#2.x=1A2B3C  o/p:123ABC

# x="1A2B3C"
# y=""
# z=""
# for i in x:
#       if i.isalpha():
#            y+=i
#       if i.isdigit():
#             z+=i
# print("alpha is string=",y)
# print("digit is string=",z)
# print(z+y)

# 3 x=[1,0,0,1,0,1,0]  o/p :0000111 in string format
# x=[1,0,0,1,0,1,0]
# a=""
# for i in x:
#    if i==0:
#       a=a+str(i)
# for i in x:

#     if i==1:
#       a=a+str(i)#
# print(a)

#4.x="hel$$lo#5#" o/p :hel$lo#5 remove only duplicates of special characters alone
# x= "hel$$lo#5#"
# y=""
# for i in x:
#     if i not in y:
#         y=y+str(i)
# print(y)

#5.print the maximum character which is occur in given string ex:HELLLOPQ o/p : maximum char in given string is L
# x="HELLLOPQ"
# my_list=list(x.upper())
# maxed_list={}
# for item in set(my_list):
#     maxed_list[item]=my_list.count(item)
#     max_char=max(maxed_list,key=maxed_list.get)
# print(max_char)

#6.x="hello python java is good"  count the number of words in given string and print output in below format
# o/p :hello5 python6 java4 is2 good4

# x="hello python java is good"
# list=x.split()
# y=[]
# for i in list:
#     y.append(i+str(len(i)))
# print(' '.join(y))



#7.x='Hello javA Is Good' ...please make each word of first and last letter if it is upper make lower if it is lower make upper
# x="Hello javA Is Good"
# y=x.split()
# z=[]
# for i in y:
#     a=i[0].swapcase()+i[1:-1]+i[-1].swapcase()
#     z.append(a)
# z=" ".join(z)
# print(z)

#8.x='hello java'  o/p : 'hello hello java java'
# #8.x='hello java'  o/p : 'hello hello java java'
# x='hello java'
# y=x.split()
# z=[]
# for i in y:
#     z.append(i +" "+ i)
# z=" ".join(z)
# print(z)


# 9.swap commas to dots and dots to commas
# Input : 14, 625, 498.002
# Output : 14.625.498, 002

# x='14,625,498.002'
# y=[]
# for i in x:
#     if i==",":
#       y.append(".")
#     elif i==".":
#       y.append(",")
#     else:
#        y.append(i)
# y="".join(y)
# print(y)


#10.x='12&&3AB$&+'   o/p :&&$&+ print only special characters from string
# x='12&&3AB$&+'
# y=x.split()
# z=[]
# for i in x:
#     if i.isalnum():
#         pass
#     else:
#        z.append(i)
# z="".join(z)
# print(z)






