// LeetCode 0070 - Climbing Stairs
// https://leetcode.com/problems/climbing-stairs/

class Solution {
    func climbStairs(_ n: Int) -> Int {
        if n <= 2 {
            return n
        }

        var prev = 1
        var curr = 2

        for _ in 3...n {
            let next = prev + curr
            prev = curr
            curr = next
        }

        return curr
    }
}
