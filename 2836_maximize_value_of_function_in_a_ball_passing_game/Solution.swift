// LeetCode 2836 - Maximize Value of Function in a Ball Passing Game
// https://leetcode.com/problems/maximize-value-of-function-in-a-ball-passing-game/

class Solution {
    func getMaxFunctionValue(_ receiver: [Int], _ k: Int) -> Int {
        let n = receiver.count
        let log = 36
        var up = Array(repeating: Array(repeating: 0, count: n), count: log)
        var sum = Array(repeating: Array(repeating: 0, count: n), count: log)
        for i in 0..<n {
            up[0][i] = receiver[i]
            sum[0][i] = receiver[i]
        }
        for j in 1..<log {
            for i in 0..<n {
                let mid = up[j - 1][i]
                up[j][i] = up[j - 1][mid]
                sum[j][i] = sum[j - 1][i] + sum[j - 1][mid]
            }
        }
        var ans = 0
        for i in 0..<n {
            var cur = i
            var total = i
            for j in 0..<log {
                if (k & (1 << j)) != 0 {
                    total += sum[j][cur]
                    cur = up[j][cur]
                }
            }
            ans = max(ans, total)
        }
        return ans
    }
}
