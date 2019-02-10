n = int(input())
while n > 0:
    cleartext = input().strip().upper().replace(' ', '')
    l = len(cleartext)
    ciphertext = [' ' for _ in range(l)]
    block, offset = 0, 0
    for letter in cleartext:
        if block * n + offset >= l:
            block = 0
            offset += 1
        ciphertext[block*n+offset] = letter
        block += 1
    print(''.join(ciphertext))
    n = int(input())
