// LeetCode 2811 - Check if it is Possible to Split Array
// https://leetcode.com/problems/check-if-it-is-possible-to-split-array/

class Solution {
    func canSplitArray(_ nums: [Int], _ m: Int) -> Bool {
        let n = nums.count
        if n <= 2 { return true }
        for i in 0..<(n - 1) where nums[i] + nums[i + 1] >= m { return true }
        return false
    }
}
