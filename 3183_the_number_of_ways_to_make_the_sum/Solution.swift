// LeetCode 3183 - The Number of Ways to Make the Sum
// https://leetcode.com/problems/the-number-of-ways-to-make-the-sum/

class Solution {
    func numberOfWays(_ n: Int) -> Int {
        let mod = 1_000_000_007
        let coins = [1, 2, 6]
        var f = Array(repeating: 0, count: n + 1)
        f[0] = 1
        for x in coins {
            if x <= n {
                for j in x...n { f[j] = (f[j] + f[j - x]) % mod }
            }
        }
        var ans = f[n]
        if n >= 4 { ans = (ans + f[n - 4]) % mod }
        if n >= 8 { ans = (ans + f[n - 8]) % mod }
        return ans
    }
}
