// LeetCode 2809 - Minimum Time to Make Array Sum At Most x
// https://leetcode.com/problems/minimum-time-to-make-array-sum-at-most-x/

class Solution {
    func minimumTime(_ nums1: [Int], _ nums2: [Int], _ x: Int) -> Int {
        let n = nums1.count
        var arr = (0..<n).map { (nums1[$0], nums2[$0]) }
        arr.sort { $0.1 < $1.1 }
        let sum1 = nums1.reduce(0, +)
        let sum2 = nums2.reduce(0, +)
        var dp = Array(repeating: 0, count: n + 1)
        for i in 0..<n {
            for j in stride(from: i + 1, through: 1, by: -1) {
                dp[j] = max(dp[j], dp[j - 1] + arr[i].0 + j * arr[i].1)
            }
        }
        for t in 0...n where sum1 + sum2 * t - dp[t] <= x { return t }
        return -1
    }
}
