// LeetCode 2401 - Longest Nice Subarray
// https://leetcode.com/problems/longest-nice-subarray/

class Solution {
    func longestNiceSubarray(_ nums: [Int]) -> Int {
        var used = 0, left = 0, ans = 0
        for right in 0..<nums.count {
            while (used & nums[right]) != 0 {
                used ^= nums[left]
                left += 1
            }
            used |= nums[right]
            ans = max(ans, right - left + 1)
        }
        return ans
    }
}
