def search(mat,k):
    row = len(mat) - 1
    col = len(mat[0]) - 1
    low = mat[0][0]
    high = mat[row][col]
    while low < high:
        mid = (low + high) // 2

        # Staircase to find number of element less than mid
        i = row
        j = 0
        count = 0
        while i >=0 and j <= col:
            if mat[i][j] <=  mid:
                count += i+1
                j += 1
            else:
                i -= 1

        if count < k:
            low = mid + 1
        elif count >= k:
            high = mid
    return low

matrix=  [[1, 5, 9],
        [10, 11, 13],
        [12, 13, 15]]
print(search(matrix,6))