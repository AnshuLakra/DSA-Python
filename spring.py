# men = 37550.0
# child = men/3

# ticket_men = men * 3
# ticket_child = child * 1
# total_without_tax = ticket_men + ticket_child
# tax = 7
# tax_of_all_tiket = total_without_tax*7/100

# after_tax = tax_of_all_tiket + total_without_tax

# offer = after_tax*10/100

# final = after_tax - offer
# print(final)



# def find_product(num1,num2,num3):
#     product=0
#     if num1 == 7:
#         product = num2 * num3
#     elif num2 == 7:
#         product = num3
#     elif num3 == 7:
#         product = -1
#     else:
#         product = num1 * num2 * num3
#     return product

# product=find_product(7,6,2)
# print(product)

# def make_amount(rupees_to_make,no_of_five,no_of_one):
#     five_needed=0
#     one_needed=0
#     five = 5 * no_of_five
#     one = 1 * no_of_one
#     total_given = five + one


#     test = rupees_to_make//5
#     total = test * 5
#     left = rupees_to_make - total
#     if total_given - rupees_to_make < 0:
#         print(-1)
#     else:
#         print("five",test)
#         print("One",left)



# make_amount(28,8,5)


# def make_amount(rupees_to_make,no_of_five,no_of_one):
#     five_needed=0
#     one_needed=0

#     #Start writing your code here
#     #Populate the variables: five_needed and one_needed
#     five = 5 * no_of_five
#     one = 1 * no_of_one
#     total_given = five + one

#     # Use the below given print statements to display the output
#     # Also, do not modify them for verification to work
#     five_needed = rupees_to_make//5
#     total = five_needed * 5
#     one_needed = rupees_to_make - total
    
#     if total_given - rupees_to_make < 0:
#         print(-1)
#     else:
#         if five_needed > no_of_five or one_needed > one:
#             print(-1)
#         else:
#             print("No. of Five needed :", five_needed)
#             print("No. of One needed  :", one_needed)
#     # print(-1)


# #Provide different values for rupees_to_make,no_of_five,no_of_one and test your program
# make_amount(105,20,5)




# def get_count(num_list):
#     count=0

#     # Write your logic here
#     for i in range(1,len(num_list)):
#         if num_list[i] == num_list[i-1]:
#             count += 1
#     return count

# #provide different values in list and test your program
# # num_list=[1,1,5,100,-20,-20,6,0,0]
# num_list =[98, 97, 97, 98]
# print(get_count(num_list))



