// LeetCode 0509 - Fibonacci Number
// https://leetcode.com/problems/fibonacci-number/

class Solution {
    func fib(_ n: Int) -> Int {
        if n <= 1 {
            return n
        }
        var previous = 0
        var current = 1
        if n >= 2 {
            for _ in 2...n {
                let next = previous + current
                previous = current
                current = next
            }
        }
        return current
    }
}
