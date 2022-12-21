''' 
2.1	Integer List
Write a Python program that accept a list of integers and check the length and the fifth element. Return true if the length of the list is 8 and fifth element occurs thrice in the said list. 
'''

int_list = []
print("Enter length of the list:")
list_len=int(input())
print("Enter numbers:")
for i in range(list_len):
    int_list.append(int(input()))
if(list_len==8):
    if(int_list.count(int_list[4])==3):
        print("True")
    else:
        print("False")
else:
    print("False")