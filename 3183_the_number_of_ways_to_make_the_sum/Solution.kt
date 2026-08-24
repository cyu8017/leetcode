// LeetCode 3183 - The Number of Ways to Make the Sum
// https://leetcode.com/problems/the-number-of-ways-to-make-the-sum/

class Solution {
    fun numberOfWays(n: Int): Int {
        val mod = 1000000007
        var coins = { 1, 2, 6 }
        var f = IntArray(n + 1)
        f[0] = 1
        for (x in coins) {
            for (j in x ..n) { f[j] = (f[j] + f[j - x]) % mod }
        }
        var ans = f[n]
        if (n >= 4) ans = (ans + f[n - 4]) % mod
        if (n >= 8) ans = (ans + f[n - 8]) % mod
        return ans
    }
}
