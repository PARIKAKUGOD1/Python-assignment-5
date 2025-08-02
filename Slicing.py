my_list = []

for num in range(1, 11):
    my_list.append(num)

print("Original list:", my_list)

sub_list = my_list[:5]
print("Extracted first five elements:", sub_list)

sub_list.reverse()
print("Reversed extracted elements:", sub_list)
