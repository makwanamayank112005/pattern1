# Pattern 1  Right Trianglr
# *
# * *
# * * *
# * * * *
# * * * * *


# n = int(input("ENter the value of n to print pattern:"))

# for i in range(0, n):
#     for j in range(0, i+1):
#         print("*", end="")
#     print()


# for i in range(1,6):
#     print("*" * i)
# Pattern 2
# * * * * *   Reverse Triangel
# * * * *
# * * *
# * *
# *

# n = int(input("ENter the value of n to print pattern:"))

# for i in range(n):
#     for j in range(n-i-1, -1, -1):
#         print("*", end="")
#     print()

# # OR

# for i in range(n-1, -1, -1):
#     for j in range(0, i+1):
#         print("*", end="")
#     print()

# for i in range(5,0,-1):
#     print("*" * i)

# pattern 3   square
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *

# for i in range(5):
#     # print("*" * 5)
#     for j in range(5):
#         print("*", end="")
#     print()

# pattern 4  Right side Triangle
#         *   
#       * *
#     * * *
#   * * * *
# * * * * *

# for i in range(0,5):
#  print(" " * (5-i-1) + "*" * (i+1))


# for i in range(0,5):
#     for j in range(5-i):
#      print(" ", end = "")
#     for j in range(i+1):
#      print("*", end = "")
#     print()

# pattern 5 Pyramid
#         *
#       * * *
#      * * * * *
#    * * * * * * * 
#  * * * * * * * * * 

# for i in range(1,6):
#     print(" " * (5 -i) + "*" *(2 *i-1))
 
# for i in range(1,6):
#     for j in range(5-i):
#         print(" ",end ="")
#     for j in range(2*i-1):
#         print("*" ,end= "")
#     print()
# pattern 6   Diamond
#         *
#       * * *
#      * * * * *
#    * * * * * * * 
#  * * * * * * * * * 
#   * * * * * * *
#     * * * * *
#      * * *
#        *

# for i in range (1,6):
#     print(" " * (5 -i) + "*" * (2*i-1))

# for i in range (6,0,-1):
#     print(" " * (5 -i)+ "*" + (2*i-1))


# for i in range (1,6):
#     for j in range(5-i):
#         print(" ",end=" ")
#     for j in range(2*i-1):
#         print("*",end =" ")
#     print()
# for i in range (4,0,-1):
#     for j in range(5-i):
#         print(" ",end=" ")
#     for j in range(2*i-1):
#         print("*",end =" ")
#     print()


# pattern 1 Number pattern

# 1
# 22
# 333
# 4444
# 55555

# for i in range(1,6):
#     print(str(i) * i)

# for i in range(0,6):
#     for j in range(0, i):
#         print(i, end="")
#     print()

# pattern 2 Reverse Number
# 555555
# 4444
# 333
# 22
# 1

# for i in range(5,0,-1):
#     print(str(i) * i)


# for i in range(5,0,-1):
#     for j in range(0,i):
#         print(i,end= "")
#     print()
# pattern 3 Triangle
# 1
# 23
# 456
# 78910

# num =1
# for i in range(1,5):
#     for j in range(i):
#         print(num,end="")
#         num =num +1
#     print()
    
# n =1
# num=0
# for i in range(1,6):
#     for j in range(i):
#         num +=1
#         print(num,end=" ")
#     print()


# pattern 4 same number Triangel
# 1
# 22
# 333
# 4444
# 55555


# for i in range(1,6):
#     for j in range(i):
#         print(i,end= "")
#     print()


# pattern 5 Incresing number pattern
# 1
# 23
# 345
# 4567
# 56789

# for i in range(1,6):
#     for j in range(i):
#         print(i +j ,end="")
#     print()

# pattern 6 Multiplication Number
# 1
# 2 4 
# 3 6 9 
# 4 8 12 16
# 5 10 15 20 25

# for i in range(1,7):
#     for j in range(1,i+1):
#         print(i * j,end=" ")
#     print()



#     1
#    21
#   321
#  4321
# 54321


#     1
#    2 2
#   3 3 3
#  4 4 4 4
# 5 5 5 5 5


#   *
#  *A*
#  *A*A*
#  *A*A*A*
# *A*A*A*A


# 1
# 212
# 32123
# 4321234  

# 11111
# 1   1
# 1   1 
# 1   1
# 11111

# 1
# 23
# 456
# 78910
# 1112131415
# 161718192021
# 22232425262728
# 2930313233343536
# 373839404142434445
# 46474849505152535455


#     1
#    1 1
#   1 2 1
#  1 3 3 1
# 1 4 6 4 1


#      1
#    2 3 2
#  3 4 5 4 3
# 4 5 6 7 6 5 4
# 5 6 7 8 9 8 7 6 5


#     *
#    **
#   ***
#  ****
# *****
#  ****
#   ***
#    **
#     *


# 1        1
# 12      21
# 123    321
# 1234  4321
# 1234554321


#     1
#    123
#   12345
#  1234567
# 123456789 
#  1234567
#   12345
#    123
#     1


# 1
# 24
# 369
# 481216
# 5105152025
# 61218243036
# 7142128354249
# 816243240485664
# 91827364554637281
# 102030405060708090100



#        ********
#       *     *
#      *     *
#     *     *
#    *     *
#   *     *
#  *     *
# ********  



# for i in range(5,0,-1):
#     for j in range(i):
#         print(" *",end="")
#     for j in range(5,1,-1):
#         print("i*j",end=" ")




for i in range(1, 6):
    print(" " * (5 - i), end="")
    for j in range(i, 0, -1):
        print(j, end="")
    print()