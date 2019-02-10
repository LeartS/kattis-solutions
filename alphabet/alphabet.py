string = input()
longest_chain = [1 for _ in string]
for i, l in enumerate(string):
    for j in range(i):
        if string[j] < l:
            longest_chain[i] = max(longest_chain[j] +1, longest_chain[i])
print(26 - max(longest_chain))