// LeetCode 3818 - Minimum Prefix Removal To Make Array Strictly Increasing
// https://leetcode.com/problems/minimum-prefix-removal-to-make-array-strictly-increasing/

class Solution {
    func minimumPrefixLength(_ nums: [Int]) -> Int {
        for i in stride(from: nums.count - 1, through: 1, by: -1) {
            if nums[i - 1] >= nums[i] { return i }
        }
        return 0
    }
}
