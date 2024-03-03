def solution(A):
    
    total_bricks = sum(A)
    if total_bricks % len(A) != 0:

        return -1

    target_bricks = total_bricks // len(A)
    moves = 0

    for bricks in A:
        difference = bricks - target_bricks
        if difference > 0:
            moves += abs(difference)

    return moves