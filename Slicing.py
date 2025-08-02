list = []

for num in range(11):
    list.append(num)

print("original list:", list)
sub_list = list[:6]
print("Extracted first five elements:", sub_list)
sub_list.reverse()
print("Reversed extracted elements", sub_list)

