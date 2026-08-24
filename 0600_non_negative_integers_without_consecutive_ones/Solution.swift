// LeetCode 0600 - Non-negative Integers without Consecutive Ones
// https://leetcode.com/problems/non-negative-integers-without-consecutive-ones/

class Solution {
    func findIntegers(_ n: Int) -> Int {
        var fib = Array(repeating: 0, count: 32)
        fib[0] = 1
        fib[1] = 2
        for i in 2..<32 { fib[i] = fib[i - 1] + fib[i - 2] }
        var answer = 0
        var prevBit = 0
        for bit in stride(from: 30, through: 0, by: -1) {
            if (n & (1 << bit)) != 0 {
                answer += fib[bit]
                if prevBit == 1 { return answer }
                prevBit = 1
            } else {
                prevBit = 0
            }
        }
        return answer + 1
    }
}
