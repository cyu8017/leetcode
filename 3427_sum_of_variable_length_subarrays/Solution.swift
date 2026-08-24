// LeetCode 3427 - Sum of Variable Length Subarrays
// https://leetcode.com/problems/sum-of-variable-length-subarrays/

class Solution {
    func subarraySum(_ nums: [Int]) -> Int {
        let n = nums.count
        var pref = Array(repeating: 0, count: n + 1)
        for i in 0..<n { pref[i + 1] = pref[i] + nums[i] }
        var ans = 0
        for i in 0..<n {
            var start = i - nums[i]
            if start < 0 { start = 0 }
            ans += pref[i + 1] - pref[start]
        }
        return ans
    }
}
