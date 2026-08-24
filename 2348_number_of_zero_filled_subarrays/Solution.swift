// LeetCode 2348 - Number of Zero-Filled Subarrays
// https://leetcode.com/problems/number-of-zero-filled-subarrays/

class Solution {
    func zeroFilledSubarray(_ nums: [Int]) -> Int {
        var ans = 0, streak = 0
        for x in nums {
            if x == 0 { streak += 1; ans += streak }
            else { streak = 0 }
        }
        return ans
    }
}
