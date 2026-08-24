// LeetCode 3151 - Special Array I
// https://leetcode.com/problems/special-array-i/

class Solution {
    func isArraySpecial(_ nums: [Int]) -> Bool {
        for i in 1..<nums.count {
            if nums[i] % 2 == nums[i - 1] % 2 { return false }
        }
        return true
    }
}
