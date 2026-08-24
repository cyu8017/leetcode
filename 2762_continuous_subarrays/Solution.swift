// LeetCode 2762 - Continuous Subarrays
// https://leetcode.com/problems/continuous-subarrays/

class Solution {
    func continuousSubarrays(_ nums: [Int]) -> Int {
        var ans = 0, left = 0
        var freq: [Int: Int] = [:]
        for right in nums.indices {
            freq[nums[right], default: 0] += 1
            while let mn = freq.keys.min(), let mx = freq.keys.max(), mx - mn > 2 {
                let v = nums[left]
                freq[v]! -= 1
                if freq[v] == 0 { freq.removeValue(forKey: v) }
                left += 1
            }
            ans += right - left + 1
        }
        return ans
    }
}
