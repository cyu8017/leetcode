// LeetCode 3320 - Count the Number of Winning Sequences
// https://leetcode.com/problems/count-the-number-of-winning-sequences/

class Solution {
    fun countWinningSequences(s: String): Int {
        val mod = 1000000007
        val n = s.length
        val mp = IntArray(256)
        mp['F'.code] = 0
        mp['W'.code] = 1
        mp['E'.code] = 2
        val beat = intArrayOf(2, 0, 1)
        val score = Array(3) { IntArray(3) }
        for (a in 0 until 3) {
            for (b in 0 until 3) {
                score[a][b] = when {
                    a == b -> 0
                    beat[a] == b -> 1
                    else -> -1
                }
            }
        }
        val offset = n
        var dp = Array(3) { IntArray(2 * n + 1) }
        val b0 = mp[s[0].code]
        for (a in 0 until 3) dp[a][score[a][b0] + offset] = 1
        for (i in 1 until n) {
            val ndp = Array(3) { IntArray(2 * n + 1) }
            val b = mp[s[i].code]
            for (last in 0 until 3) {
                for (d in 0..2 * n) {
                    if (dp[last][d] == 0) continue
                    for (a in 0 until 3) {
                        if (a == last) continue
                        val nd = d + score[a][b]
                        if (nd < 0 || nd > 2 * n) continue
                        ndp[a][nd] = (ndp[a][nd] + dp[last][d]) % mod
                    }
                }
            }
            dp = ndp
        }
        var ans = 0
        for (a in 0 until 3) {
            for (d in offset + 1..2 * n) ans = (ans + dp[a][d]) % mod
        }
        return ans
    }
}
