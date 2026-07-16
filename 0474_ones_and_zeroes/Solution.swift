// LeetCode 0474 - Ones and Zeroes
// https://leetcode.com/problems/ones-and-zeroes/

class Solution {
    func findMaxForm(_ strs: [String], _ m: Int, _ n: Int) -> Int {
        var dp = Array(repeating: Array(repeating: 0, count: n + 1), count: m + 1)
        for string in strs {
            let zeros = string.filter { $0 == "0" }.count
            let ones = string.filter { $0 == "1" }.count
            var zero = m
            while zero >= zeros {
                var one = n
                while one >= ones {
                    dp[zero][one] = max(dp[zero][one], dp[zero - zeros][one - ones] + 1)
                    one -= 1
                }
                zero -= 1
            }
        }
        return dp[m][n]
    }
}
