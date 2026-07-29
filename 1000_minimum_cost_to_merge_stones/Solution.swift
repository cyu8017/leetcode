// LeetCode 1000 - Minimum Cost to Merge Stones
// https://leetcode.com/problems/minimum-cost-to-merge-stones/

class Solution {
    func mergeStones(_ stones: [Int], _ k: Int) -> Int {
        let n = stones.count
        if (n - 1) % (k - 1) != 0 { return -1 }
        var prefix = [0]
        for x in stones { prefix.append(prefix.last! + x) }
        var dp = Array(repeating: Array(repeating: 0, count: n), count: n)
        for length in k...n {
            for i in 0...(n - length) {
                let j = i + length - 1
                var best = Int.max
                var m = i
                while m < j {
                    best = min(best, dp[i][m] + dp[m + 1][j])
                    m += k - 1
                }
                dp[i][j] = best
                if (length - 1) % (k - 1) == 0 {
                    dp[i][j] += prefix[j + 1] - prefix[i]
                }
            }
        }
        return dp[0][n - 1]
    }
}
