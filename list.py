#create a list with 10 elements.

number_list = [1,2,3,4,5,6,7,8,9,10]
print("Original list: ",number_list)

#Extract first five element from list.
extract_list = number_list[:5]
print("Extracted first five elements: ",extract_list)

#extracted elements in reversed item.
reverse_list = list(reversed(extract_list))
print("Reversed extracted list: ",reverse_list)