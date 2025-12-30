def calculate_impact(contributions : list):
    n = len(contributions)
    if n == 1:
        return [1]
    impact = [0] * n

# Calculating Left: left[i] contains product of left side of list including itself.
    left = [1] *  n
    left_prod = 1
    for i in range(n):
        left_prod *= contributions[i]
        left[i] = left_prod

# Calculating Right: right[i] contains product of right side of list including itself.
    right = [1] * n
    right_prod = 1
    for i in range(n-1,-1,-1):
        right_prod *= contributions[i]
        right[i] = right_prod

# Calculating Impact:
    impact[0] = right[1]
    impact[-1] = left[-2]
    for j in range(1,n-1):
        impact[j] = left[j-1] * right[j+1]

    return impact

# Example 1:
# Contributions = [1, 2, 3, 4]
# Impact = calculate_impact(Contributions)
# print(Impact)

# Example 2:
# Contributions = [-1, 1, 0, -3, 3]
# Impact = calculate_impact(Contributions)
# print(Impact)
