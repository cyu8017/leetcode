// LeetCode 1416 - Restore The Array
// https://leetcode.com/problems/restore-the-array/

class Solution {
    func numberOfArrays(_ s: String, _ k: Int) -> Int {
        let mod = 1_000_000_007
        let chars = Array(s), n = chars.count
        var dp = Array(repeating: 0, count: n + 1)
        dp[n] = 1
        for i in stride(from: n - 1, through: 0, by: -1) {
            if chars[i] == "0" { continue }
            var value = 0
            for j in i..<n {
                value = value * 10 + Int(String(chars[j]))!
                if value > k { break }
                dp[i] = (dp[i] + dp[j + 1]) % mod
            }
        }
        return dp[0]
    }
}
