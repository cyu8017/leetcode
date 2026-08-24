// LeetCode 2871 - Split Array Into Maximum Number of Subarrays
// https://leetcode.com/problems/split-array-into-maximum-number-of-subarrays/

class Solution {
    func maxSubarrays(_ nums: [Int]) -> Int {
        var ans = 0
        var cur = -1
        for v in nums {
            if cur == -1 { cur = v }
            else { cur &= v }
            if cur == 0 {
                ans += 1
                cur = -1
            }
        }
        return ans == 0 ? 1 : ans
    }
}
