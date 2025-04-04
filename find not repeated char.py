#returns the first character that does not repeat.
input =  "leetcode"

length = len(input)
# print(length)

for i in  range (length):
    #print(input[i])
    i += 1
    if input[0] != input[i]:
        print(input[0])
        break

# output:
# l