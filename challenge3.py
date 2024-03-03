def solution(N):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    result = ''
    
    
    full_repetitions = N // 26
    remainder = N % 26

    for i in range(26):
        if i < remainder:
            result += alphabet[i] * (full_repetitions + 1)
        else:
            result += alphabet[i] * full_repetitions
    
    return result[:N] 