// LeetCode 2958 - Length of Longest Subarray With at Most K Frequency
// https://leetcode.com/problems/length-of-longest-subarray-with-at-most-k-frequency/

class Solution {
    func maxSubarrayLength(_ nums: [Int], _ k: Int) -> Int {
        var freq: [Int: Int] = [:]
        var ans = 0, left = 0
        for right in 0..<nums.count {
            freq[nums[right], default: 0] += 1
            while freq[nums[right]]! > k {
                freq[nums[left], default: 0] -= 1
                left += 1
            }
            ans = max(ans, right - left + 1)
        }
        return ans
    }
}
