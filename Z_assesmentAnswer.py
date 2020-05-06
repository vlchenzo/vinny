# print("\n6.) Write a program that will print:")
# print("\ta.) 'A' for multiples of 3")
# print("\ta.) 'B' for multiples of 5")
# print("\ta.) 'C' for multiples of 7")
# print("If a number is a multiple of several factors, print all letters.")
# print("e.g. 21 is a multiple of both 3 and 7, so print AC")
# answer for 6

# i =0
#
# while True:
#     if i < 99:
#         i = i + 1
#         print (i)
#         var = "this number is not a mod of 3,5, or 7"
#         if ((i % 3) == 0):
#             var = "A"
#         if ((i % 5) == 0):
#             var = "B"
#         if ((i % 7) == 0):
#             var = "C"
#         print(var)
#     else:
#         break
# print ('we reached: ',i)


i =0
multiple_of_3 = [3,6,9,12,15,18,21,24,27,30,33,36,39,42,45,48,51,54,57,60,63,66,69,72,75,78,81,84,87,90,93,96,99]
multiple_of_5 = [5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100]
multiple_of_7 = [7,14,21,28,35,42,49,56,63,70,77,84,91,98,105]
multiple_of_3or5 = [15, 30, 45, 60, 75, 90]
multiple_of_3or7 = [21, 42, 63,84]
while True:
    if i < 99:
        i = i + 1

        var = str(i) + " (this number is not a mod of 3,5, or 7)"
        if i == multiple_of_3or7:
            # var = str(i) +" (AC)"
            print("AC")
        elif i == multiple_of_3:
            print("A")
        # elif ((i % 3) == 0):
        #     var = str(i) +" (A)"
        # elif ((i % 5) == 0):
        #     var = str(i) +" (B)"
        # elif ((i % 7) == 0):
        #     var = str(i) +" (C)"

        print(var)
    else:
        break
print ('we reached: ',i)
