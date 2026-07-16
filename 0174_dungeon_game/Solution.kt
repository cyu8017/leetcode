class Solution {
    fun calculateMinimumHP(dungeon: Array<IntArray>): Int {
        val rows = dungeon.size
        val cols = dungeon[0].size
        val dp = Array(rows + 1) { IntArray(cols + 1) { Int.MAX_VALUE } }
        dp[rows][cols - 1] = 1
        dp[rows - 1][cols] = 1

        for (r in rows - 1 downTo 0) {
            for (c in cols - 1 downTo 0) {
                val needed = minOf(dp[r + 1][c], dp[r][c + 1]) - dungeon[r][c]
                dp[r][c] = maxOf(1, needed)
            }
        }
        return dp[0][0]
    }
}
