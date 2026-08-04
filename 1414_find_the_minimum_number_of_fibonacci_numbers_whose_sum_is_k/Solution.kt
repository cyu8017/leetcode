// LeetCode 1414 - Find the Minimum Number of Fibonacci Numbers Whose Sum Is K
// https://leetcode.com/problems/find-the-minimum-number-of-fibonacci-numbers-whose-sum-is-k/

class Solution {
    fun findMinFibonacciNumbers(k: Int): Int {
        var remaining = k
        val fib = arrayListOf(1, 1)
        while (fib.last() < remaining) {
            fib.add(fib[fib.size - 1] + fib[fib.size - 2])
        }
        var answer = 0
        for (i in fib.size - 1 downTo 0) {
            if (fib[i] <= remaining) {
                remaining -= fib[i]
                answer++
            }
        }
        return answer
    }
}
