
#my_list = [1, 354, 99, 4553, -3, 45, 100]
#for i in my_list:
 #   if i > 100:
   #     print(i)
  #  else:
   #     pass


####################

#my_list = [1, 354, 99, 4553, -3, 45, 100]
#my_result = []
#for i in my_list:
#    if i > 100:
#        my_result.append(i)
#    else:
#        pass
#print(my_result)



#################У######################


my_list = [1, 34, 324]
if len(my_list) < 2:
    my_list.append(0)
else:
    my_list.append(my_list[-1] + my_list[-2])

print(my_list)