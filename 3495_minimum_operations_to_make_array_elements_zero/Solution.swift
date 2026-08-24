// LeetCode 3495 - Minimum Operations to Make Array Elements Zero
// https://leetcode.com/problems/minimum-operations-to-make-array-elements-zero/

class Solution {
    func minOperations(_ queries: [[Int]]) -> Int {
        var ans = 0
        for q in queries {
            var sum = 0
            for x in q[0]...q[1] { sum += opsToZero(x) }
            ans += (sum + 1) / 2
        }
        return ans
    }

    private func opsToZero(_ x: Int) -> Int {
        var x = x, ops = 0
        while x > 0 { x /= 4; ops += 1 }
        return ops
    }
}
