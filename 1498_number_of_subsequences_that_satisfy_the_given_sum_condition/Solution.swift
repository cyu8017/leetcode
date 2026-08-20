// LeetCode 1498 - Number of Subsequences That Satisfy the Given Sum Condition
// https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/

class Solution {
    func numSubseq(_ nums: [Int], _ target: Int) -> Int {
        let nums = nums.sorted()
        let mod = 1_000_000_007
        var left = 0, right = nums.count - 1, ans = 0
        var powers = Array(repeating: 1, count: nums.count + 1)
        for i in 1..<powers.count { powers[i] = powers[i - 1] * 2 % mod }
        while left <= right {
            if nums[left] + nums[right] <= target {
                ans = (ans + powers[right - left]) % mod
                left += 1
            } else {
                right -= 1
            }
        }
        return ans
    }
}
