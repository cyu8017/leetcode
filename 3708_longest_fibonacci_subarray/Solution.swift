// LeetCode 3708 - Longest Fibonacci Subarray
// https://leetcode.com/problems/longest-fibonacci-subarray/

class Solution {
    func longestSubarray(_ nums: [Int]) -> Int {
        var f = 2, ans = f
        if nums.count > 2 {
            for i in 2..<nums.count {
                if nums[i] == nums[i - 1] + nums[i - 2] {
                    f += 1
                    ans = max(ans, f)
                } else { f = 2 }
            }
        }
        return ans
    }
}
