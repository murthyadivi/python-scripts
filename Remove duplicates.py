# This function checks the contents of a list and removes duplicates
def remove_duplicates(x):
  check_list = []
  for i in x:
    if i not in check_list:
      check_list.append(i)
  return check_list



list = [2,3,4,3,2,5,6,7,4,5,9]
print (list)
print (remove_duplicates(list))
