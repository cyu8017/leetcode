// LeetCode 2936 - Number of Equal Numbers Blocks
// https://leetcode.com/problems/number-of-equal-numbers-blocks/

class Solution {
    func blockCount(_ nums: [Int]) -> Int {
        if nums.isEmpty { return 0 }
        var ans = 1
        for i in 1..<nums.count where nums[i] != nums[i - 1] {
            ans += 1
        }
        return ans
    }
}
