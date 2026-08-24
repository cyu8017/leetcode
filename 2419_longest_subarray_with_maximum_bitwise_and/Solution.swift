// LeetCode 2419 - Longest Subarray With Maximum Bitwise AND
// https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and/

class Solution {
    func longestSubarray(_ nums: [Int]) -> Int {
        let mx = nums.max()!
        var ans = 0, cur = 0
        for x in nums {
            if x == mx {
                cur += 1
                ans = max(ans, cur)
            } else {
                cur = 0
            }
        }
        return ans
    }
}
