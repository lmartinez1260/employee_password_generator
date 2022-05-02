# import random for random #'s in temp password
import random
# need to store emp's First & Last name
emp_first_name = input("Enter Full First name: ")

emp_last_name = input("Enter Full Last name: ")
# generate rand list
rand_nums = [random.randrange(1, 10, 1) for i in range(4)]
# array length must be at least of size num
def list_stringify(arr, num):
    emp_string = ""
    for i in range(num):
        emp_string += str(arr[i])
    return emp_string

# function to make temp password
def temp_pass_gen():
  

  temp_pass = emp_last_name[:4] + emp_first_name[:3] + list_stringify(rand_nums, 4)

  return temp_pass.title()

emp_pass = temp_pass_gen()

print(emp_pass)
