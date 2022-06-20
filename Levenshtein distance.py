import sys

input_word = input()
if input_word == '':
    print(0)
elif input_word.count(' ') == 0:
    print(len(input_word))
elif input_word.count(' ') == 1:
    before, after = input_word.split()

    if before.isalnum() != True or after.isalnum() != True:
        sys.exit(100)
    else:
        len_b = len(before)
        len_a = len(after)
    
        matrix = [[] for i in range(len_b+1)]

        for i in range(len_b+1):
            matrix[i] = [0 for j in range(len_a+1)]

        for i in range(len_b+1):
            matrix[i][0] = i
        for j in range(len_a+1):
            matrix[0][j] = j

        for i in range(1, len_b+1):
            a = before[i-1]
            for j in range(1, len_a+1):
                b = after[j-1]
                cost = 0 if (a == b) else 1
                matrix[i][j] = min([
                    matrix[i-1][j] + 1,
                    matrix[i][j-1] + 1,
                    matrix[i-1][j-1] + cost
                ])
        print(matrix[len_b][len_a])
else:
    sys.exit(100)