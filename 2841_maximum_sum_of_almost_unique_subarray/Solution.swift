// LeetCode 2841 - Maximum Sum of Almost Unique Subarray
// https://leetcode.com/problems/maximum-sum-of-almost-unique-subarray/

class Solution {
    func maxSum(_ nums: [Int], _ m: Int, _ k: Int) -> Int {
        var freq: [Int: Int] = [:]
        var sum = 0, ans = 0
        for i in 0..<nums.count {
            freq[nums[i], default: 0] += 1
            sum += nums[i]
            if i >= k {
                let out = nums[i - k]
                sum -= out
                freq[out, default: 0] -= 1
                if freq[out] == 0 { freq.removeValue(forKey: out) }
            }
            if i >= k - 1 && freq.count >= m {
                ans = max(ans, sum)
            }
        }
        return ans
    }
}
