// LeetCode 1043 - Partition Array for Maximum Sum
// https://leetcode.com/problems/partition-array-for-maximum-sum/

class Solution {
    func maxSumAfterPartitioning(_ arr: [Int], _ k: Int) -> Int {
        let n = arr.count
        var dp = Array(repeating: 0, count: n + 1)
        for i in 1...n {
            var best = 0
            for size in 1...min(k, i) {
                best = max(best, arr[i - size])
                dp[i] = max(dp[i], dp[i - size] + best * size)
            }
        }
        return dp[n]
    }
}
