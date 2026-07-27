// LeetCode 1690 - Stone Game VII
// https://leetcode.com/problems/stone-game-vii/

class Solution {
    func stoneGameVII(_ stones: [Int]) -> Int {
        let n = stones.count
        var pre = [0]
        for x in stones { pre.append(pre.last! + x) }
        var dp = Array(repeating: Array(repeating: 0, count: n), count: n)
        for length in 2...n {
            for i in 0...(n - length) {
                let j = i + length - 1
                dp[i][j] = max(pre[j + 1] - pre[i + 1] - dp[i + 1][j], pre[j] - pre[i] - dp[i][j - 1])
            }
        }
        return dp[0][n - 1]
    }
}
