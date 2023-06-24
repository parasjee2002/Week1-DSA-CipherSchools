def generateParenthesis(n):
    def backtrack(s, left, right):
        if left == 0 and right == 0:
            result.append(s)
            return
        if left > 0:
            backtrack(s + '(', left - 1, right)
        if right > left:
            backtrack(s + ')', left, right - 1)

    result = []
    backtrack('', n, n)
    return result

n = 3
result = generateParenthesis(n)
print(result)
