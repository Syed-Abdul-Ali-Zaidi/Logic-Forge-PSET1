def calculate_impact(contributions : list):
    n = len(contributions)
    if n == 1:
        return [1]
    impact = [0] * n

# Calculating Left: left[i] contains product of left side of list including itself.
    left = [1] *  n
    left[0] = contributions[0]
    for i in range(1,n):
        left[i] = left[i-1] * contributions[i]

# Calculating Right: right[i] contains product of right side of list including itself.
    right = [1] * n
    right[-1] = contributions[-1]
    for i in range(n-2,-1,-1):
        right[i] = right[i+1] * contributions[i]

# Calculating Impact:
    impact[0] = right[1]
    impact[-1] = left[-2]
    for j in range(1,n-1):
        impact[j] = left[j-1] * right[j+1]

    return impact
