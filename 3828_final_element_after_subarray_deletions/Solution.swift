// LeetCode 3828 - Final Element After Subarray Deletions
// https://leetcode.com/problems/final-element-after-subarray-deletions/

class Solution {
    func finalElement(_ nums: [Int]) -> Int {
        return max(nums[0], nums[nums.count - 1])
    }
}
