// LeetCode 3496 - Maximize Score After Pair Deletions
// https://leetcode.com/problems/maximize-score-after-pair-deletions/

class Solution {
    func maximizeScore(_ nums: [Int]) -> Int {
        let n = nums.count
        let total = nums.reduce(0, +)
        if n % 2 == 1 { return total - (nums.min() ?? 0) }
        var mn = nums[0] + nums[1]
        for i in 0..<(n - 1) { mn = min(mn, nums[i] + nums[i + 1]) }
        return total - mn
    }
}
