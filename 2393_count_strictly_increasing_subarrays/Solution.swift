// LeetCode 2393 - Count Strictly Increasing Subarrays
// https://leetcode.com/problems/count-strictly-increasing-subarrays/

class Solution {
    func countSubarrays(_ nums: [Int]) -> Int {
        var ans = 0, len = 0
        for i in 0..<nums.count {
            if i > 0 && nums[i] > nums[i - 1] { len += 1 }
            else { len = 1 }
            ans += len
        }
        return ans
    }
}
