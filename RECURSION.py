def RecursiveFunction(num):
    # Base Case: If num is 1, return 1
    if num == 1:
        return 1
    else:
        # Recursive Case: Return num + RecursiveFunction(num - 1)
        return num + RecursiveFunction(num - 1)

# Time Complexity: O(n) - The function makes n recursive calls.
# Space Complexity: O(n) - The maximum depth of the recursion stack is n.
