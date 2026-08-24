// LeetCode 2537 - Count the Number of Good Subarrays
// https://leetcode.com/problems/count-the-number-of-good-subarrays/

class Solution {
    func countGood(_ nums: [Int], _ k: Int) -> Int {
        var freq = [Int: Int]()
        var pairs = 0, ans = 0, left = 0
        for right in 0..<nums.count {
            pairs += freq[nums[right], default: 0]
            freq[nums[right], default: 0] += 1
            while pairs >= k {
                ans += nums.count - right
                freq[nums[left]]! -= 1
                pairs -= freq[nums[left]]!
                left += 1
            }
        }
        return ans
    }
}
