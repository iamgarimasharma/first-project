#Program for integer value
x=int(input("Enter any integer number"))
a=int(min(str(x)))
b=int(max(str(x)))+1
for i in range(len(str(x))-1):
    a*=10
    b*=10
k=0
for i in range(a,b):
    d=0
    for j in str(x):
        if(str(i).__contains__(j)):
            d+=1
    if(d==len(str(x))):
        print(i)
        k+=1

print("Possible combinations are:",k)


# #Program for characters
# x=input("Enter any set of character ")
# a=min(str(x))
# b=max(str(x))
# # i=len(x)
# k=0
# for e in iter(x):
#     y=e
#     for f in iter(y):
#         print(y)
# # k=0
# # for i in x:
# #
# #     d=0
# #     print(chr(i))
# #     for j in x:
# #         if(chr(i).__contains__(j)):
# #             d+=1
# #     if(d==len(x)):
# #         print(i)
# #         k+=1
# #
# # print("Possible combinations are:",k)
# #
# #
# #
#
#
#
#
#
