#2.print even numbers
# set_even={i for i in range(1,11) if i%2==0}
# print(set_even)

#3.	x=[1,4,5,3,1,4] reverse the list and remove the duplicates using set ?
# x=[1,4,5,3,1,4]
# x.reverse()
# print(x)
# y=set(x)
# print(y)
# z=x.intersection(y)
# print(z)

# 4.take two sets get unique values from set
# x={10,20,30,40,50,60}
# y={50,60,70,80,90,100}
# z=x.union(y)
# print(z)

#5. how to concatenate two sets ? write an example?
#we can use update and union function
# a={11,12,13,14,15}
# b={16,17,20,18,19}
# a.update(b)
# print(a)
# x={10,20,30,40,50,60}
# y={50,60,70,80,90,100}
# z=x.union(y)
# print(z)

#6.Write a program to get common elements from two sets?
# x={10,20,30,40,50,60}
# y={50,60,70,80,90,100}
# z=x.intersection(y)
# print(z)


# 7. write a example for tuple comprehension ?
# set_even=(i for i in range(1,11) if i%2==0)
# print(set_even)


#8. x=[6,3,2,5,1]  sort the list elements without using sort function ? op : [1,2,3,5,6]
# x=[6,3,2,5,1]
# for i in range(len(x)):
#     for j in range(i+1,len(x)):
#         if x[i]>x[j]:
#             x[i],x[j]=x[j],x[i]
# print(x)

# 9. write a program to change tuple values using list ?
# x=(1,2,3,4,5)
# y=list(x)
# print(y)
# y[3]=200
# print(y)

# 10.print the multiplication table using loops ->
# input should b taken from keyboard ?

# a=int(input("Enter the table number:"))
# for i in range(1,11):
#     print(a,"*",i,"=",a*i)

