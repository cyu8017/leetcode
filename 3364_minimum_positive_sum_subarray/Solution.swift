// LeetCode 3364 - Minimum Positive Sum Subarray
// https://leetcode.com/problems/minimum-positive-sum-subarray/

class Solution {
    func minimumSumSubarray(_ nums: [Int], _ l: Int, _ r: Int) -> Int {
        let n = nums.count
        var pref = Array(repeating: 0, count: n + 1)
        for i in 0..<n { pref[i + 1] = pref[i] + nums[i] }
        var ans = Int.max
        var found = false
        for i in 0..<n {
            var length = l
            while length <= r && i + length <= n {
                let s = pref[i + length] - pref[i]
                if s > 0 && s < ans {
                    ans = s
                    found = true
                }
                length += 1
            }
        }
        return found ? ans : -1
    }
}
