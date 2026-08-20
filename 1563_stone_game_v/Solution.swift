// LeetCode 1563 - Stone Game V
// https://leetcode.com/problems/stone-game-v/

class Solution {
    func stoneGameV(_ stoneValue: [Int]) -> Int {
        let n = stoneValue.count
        if n == 0 { return 0 }
        var pre = [0]
        for x in stoneValue { pre.append(pre.last! + x) }
        var dp = Array(repeating: Array(repeating: 0, count: n), count: n)
        var left = Array(repeating: Array(repeating: 0, count: n), count: n)
        var right = Array(repeating: Array(repeating: 0, count: n), count: n)
        for i in 0..<n {
            left[i][i] = stoneValue[i]
            right[i][i] = stoneValue[i]
        }
        for length in 2...n {
            for i in 0...(n - length) {
                let j = i + length - 1
                var lo = i, hi = j - 1
                while lo <= hi {
                    let mid = (lo + hi) / 2
                    if 2 * (pre[mid + 1] - pre[i]) >= pre[j + 1] - pre[i] {
                        hi = mid - 1
                    } else {
                        lo = mid + 1
                    }
                }
                let split = lo
                let leftSum = pre[split + 1] - pre[i]
                let rightSum = pre[j + 1] - pre[split + 1]
                var best = right[split + 1][j]
                if leftSum == rightSum {
                    best = max(best, left[i][split])
                } else if split > i {
                    best = max(best, left[i][split - 1])
                }
                dp[i][j] = best
                let total = pre[j + 1] - pre[i]
                left[i][j] = max(left[i][j - 1], total + best)
                right[i][j] = max(right[i + 1][j], total + best)
            }
        }
        return dp[0][n - 1]
    }
}
