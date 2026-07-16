class Solution:
    def findMinFibonacciNumbers(self, k):
        fib = [1, 1]
        while fib[-1] < k:
            fib.append(fib[-1] + fib[-2])
        answer = 0
        for value in reversed(fib):
            if value <= k:
                k -= value
                answer += 1
        return answer
