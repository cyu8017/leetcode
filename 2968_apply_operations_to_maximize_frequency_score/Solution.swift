// LeetCode 2968 - Apply Operations to Maximize Frequency Score
// https://leetcode.com/problems/apply-operations-to-maximize-frequency-score/

class Solution {
    func maxFrequencyScore(_ nums: [Int], _ k: Int) -> Int {
        let nums = nums.sorted()
        let n = nums.count
        var pref = Array(repeating: 0, count: n + 1)
        for i in 0..<n { pref[i + 1] = pref[i] + nums[i] }
        var ans = 1, left = 0
        for right in 0..<n {
            while cost(nums, pref, left, right) > k { left += 1 }
            ans = max(ans, right - left + 1)
        }
        return ans
    }

    private func cost(_ nums: [Int], _ pref: [Int], _ l: Int, _ r: Int) -> Int {
        let mid = (l + r) / 2
        let left = nums[mid] * (mid - l) - (pref[mid] - pref[l])
        let right = (pref[r + 1] - pref[mid + 1]) - nums[mid] * (r - mid)
        return left + right
    }
}
