// LeetCode 2302 - Count Subarrays With Score Less Than K
// https://leetcode.com/problems/count-subarrays-with-score-less-than-k/

class Solution {
    func countSubarrays(_ nums: [Int], _ k: Int) -> Int {
        var ans = 0, sum = 0, left = 0
        for right in 0..<nums.count {
            sum += nums[right]
            while sum * (right - left + 1) >= k {
                sum -= nums[left]
                left += 1
            }
            ans += right - left + 1
        }
        return ans
    }
}
