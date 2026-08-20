// LeetCode 1414 - Find the Minimum Number of Fibonacci Numbers Whose Sum Is K
// https://leetcode.com/problems/find-the-minimum-number-of-fibonacci-numbers-whose-sum-is-k/

class Solution {
    func findMinFibonacciNumbers(_ k: Int) -> Int {
        var fib = [1, 1], k = k
        while fib.last! < k { fib.append(fib[fib.count - 1] + fib[fib.count - 2]) }
        var answer = 0
        for value in fib.reversed() where value <= k {
            k -= value; answer += 1
        }
        return answer
    }
}
