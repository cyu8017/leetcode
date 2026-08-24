// LeetCode 2422 - Merge Operations to Turn Array Into a Palindrome
// https://leetcode.com/problems/merge-operations-to-turn-array-into-a-palindrome/

class Solution {
    func minimumOperations(_ nums: [Int]) -> Int {
        var l = 0, r = nums.count - 1
        var left = nums[l], right = nums[r]
        var ans = 0
        while l < r {
            if left == right {
                l += 1
                r -= 1
                if l < r {
                    left = nums[l]
                    right = nums[r]
                }
            } else if left < right {
                l += 1
                left += nums[l]
                ans += 1
            } else {
                r -= 1
                right += nums[r]
                ans += 1
            }
        }
        return ans
    }
}
