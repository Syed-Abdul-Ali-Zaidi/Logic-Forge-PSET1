def search(mat,k):
    row = len(mat) - 1
    col = len(mat[0]) - 1
    
    low = mat[0][0]    # First element
    high = mat[row][col]    # Last Element
    while low < high:
        mid = (low + high) // 2

        # Staircase to find number of element less than mid
        # Starting from bottom-left of matrix
        i = row
        j = 0
        count = 0    # No. of elements that are less than mid
        while i >=0 and j <= col:
            if mat[i][j] <=  mid:
                count += i+1    # Whole column till "i" is less than mid
                j += 1    # Move right
            else:
                i -= 1    # Move up

        if count < k:    # if True than it means that Kth smallest lies in post-mid values
            low = mid + 1
        elif count >= k:    # if True than it means that Kth smallest value is mid or lies in pre-mid values
            high = mid
    return low

# matrix=  [[1, 5, 9],
#         [10, 11, 13],
#         [12, 13, 15]]

# print(search(matrix,8))
