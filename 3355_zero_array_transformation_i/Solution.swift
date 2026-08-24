// LeetCode 3355 - Zero Array Transformation I
// https://leetcode.com/problems/zero-array-transformation-i/

class Solution {
    func isZeroArray(_ nums: [Int], _ queries: [[Int]]) -> Bool {
        let n = nums.count
        var diff = Array(repeating: 0, count: n + 1)
        for q in queries {
            diff[q[0]] += 1
            diff[q[1] + 1] -= 1
        }
        var cur = 0
        for i in 0..<n {
            cur += diff[i]
            if cur < nums[i] { return false }
        }
        return true
    }
}
