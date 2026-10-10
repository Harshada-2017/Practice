def find_max(list):
maximum = list[0]

for i in range(1, len(list)):
    if list[i] > maximum:
        maximum = list[i]

return maximum