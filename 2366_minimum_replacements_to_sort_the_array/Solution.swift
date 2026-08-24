// LeetCode 2366 - Minimum Replacements to Sort the Array
// https://leetcode.com/problems/minimum-replacements-to-sort-the-array/

class Solution {
    func minimumReplacement(_ nums: [Int]) -> Int {
        var ans = 0
        var prev = nums[nums.count - 1]
        for i in stride(from: nums.count - 2, through: 0, by: -1) {
            if nums[i] <= prev { prev = nums[i]; continue }
            let parts = (nums[i] + prev - 1) / prev
            ans += parts - 1
            prev = nums[i] / parts
        }
        return ans
    }
}
