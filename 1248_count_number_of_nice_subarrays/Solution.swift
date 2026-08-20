// LeetCode 1248 - Count Number of Nice Subarrays
// https://leetcode.com/problems/count-number-of-nice-subarrays/

class Solution {
    func numberOfSubarrays(_ nums: [Int], _ k: Int) -> Int {
        func atMost(_ k: Int) -> Int {
            var k = k
            var ans = 0, left = 0
            for right in 0..<nums.count {
                k -= nums[right] % 2
                while k < 0 {
                    k += nums[left] % 2
                    left += 1
                }
                ans += right - left + 1
            }
            return ans
        }
        return atMost(k) - atMost(k - 1)
    }
}
