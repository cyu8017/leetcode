// LeetCode 2962 - Count Subarrays Where Max Element Appears at Least K Times
// https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/

class Solution {
    func countSubarrays(_ nums: [Int], _ k: Int) -> Int {
        let mx = nums.max() ?? 0
        var ans = 0, cnt = 0, left = 0
        for right in 0..<nums.count {
            if nums[right] == mx { cnt += 1 }
            while cnt >= k {
                if nums[left] == mx { cnt -= 1 }
                left += 1
            }
            ans += left
        }
        return ans
    }
}
