// LeetCode 1493 - Longest Subarray of 1's After Deleting One Element
// https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/

class Solution {
    func longestSubarray(_ nums: [Int]) -> Int {
        var left = 0, zeros = 0, ans = 0
        for (right, x) in nums.enumerated() {
            if x == 0 { zeros += 1 }
            while zeros > 1 {
                if nums[left] == 0 { zeros -= 1 }
                left += 1
            }
            ans = max(ans, right - left)
        }
        return ans
    }
}
