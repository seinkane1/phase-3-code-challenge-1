def solution(A):
    max_sum = -1

    for i in range(len(A)):
        
        for j in range(i + 1, len(A)):
            
            sum_i = sum(int(digit) for digit in str(A[i]))
            sum_j = sum(int(digit) for digit in str(A[j]))

            if sum_i == sum_j and sum_i + sum_j > max_sum:
                max_sum = sum_i + sum_j

    return max_sum