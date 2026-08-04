// LeetCode 1444 - Number of Ways of Cutting a Pizza
// https://leetcode.com/problems/number-of-ways-of-cutting-a-pizza/

class Solution {
    fun ways(pizza: Array<String>, k: Int): Int {
        val mod = 1_000_000_007
        val rows = pizza.size
        val cols = pizza[0].length
        val apples = Array(rows + 1) { IntArray(cols + 1) }
        for (r in rows - 1 downTo 0) {
            for (c in cols - 1 downTo 0) {
                apples[r][c] = (if (pizza[r][c] == 'A') 1 else 0) +
                    apples[r + 1][c] + apples[r][c + 1] - apples[r + 1][c + 1]
            }
        }
        var dp = Array(rows) { r -> IntArray(cols) { c -> if (apples[r][c] > 0) 1 else 0 } }
        repeat(k - 1) {
            val nxt = Array(rows) { IntArray(cols) }
            for (r in 0 until rows) {
                for (c in 0 until cols) {
                    for (nr in r + 1 until rows) {
                        if (apples[r][c] > apples[nr][c]) {
                            nxt[r][c] = (nxt[r][c] + dp[nr][c]) % mod
                        }
                    }
                    for (nc in c + 1 until cols) {
                        if (apples[r][c] > apples[r][nc]) {
                            nxt[r][c] = (nxt[r][c] + dp[r][nc]) % mod
                        }
                    }
                }
            }
            dp = nxt
        }
        return dp[0][0]
    }
}
