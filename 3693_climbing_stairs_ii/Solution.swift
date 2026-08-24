// LeetCode 3693 - Climbing Stairs II
// https://leetcode.com/problems/climbing-stairs-ii/

class Solution {
    func climbStairs(_ n: Int, _ costs: [Int]) -> Int {
        let inf = 1_000_000_000
        var f = Array(repeating: inf, count: n + 1)
        f[0] = 0
        for i in 1...n {
            let x = costs[i - 1]
            for j in max(0, i - 3)..<i {
                f[i] = min(f[i], f[j] + x + (i - j) * (i - j))
            }
        }
        return f[n]
    }
}
