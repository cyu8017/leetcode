// LeetCode 1770 - Maximum Score from Performing Multiplication Operations
// https://leetcode.com/problems/maximum-score-from-performing-multiplication-operations/

class Solution {
    func maximumScore(_ nums: [Int], _ multipliers: [Int]) -> Int {
        let n = nums.count
        let m = multipliers.count
        var next = [Int](repeating: 0, count: m + 1)
        for i in stride(from: m - 1, through: 0, by: -1) {
            var cur = [Int](repeating: 0, count: m + 1)
            for left in stride(from: i, through: 0, by: -1) {
                let right = n - 1 - (i - left)
                let takeLeft = nums[left] * multipliers[i] + next[left + 1]
                let takeRight = nums[right] * multipliers[i] + next[left]
                cur[left] = max(takeLeft, takeRight)
            }
            next = cur
        }
        return next[0]
    }
}
