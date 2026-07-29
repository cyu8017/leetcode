// LeetCode 1079 - Letter Tile Possibilities
// https://leetcode.com/problems/letter-tile-possibilities/

class Solution {
    fun numTilePossibilities(tiles: String): Int {
        val count = IntArray(26)
        for (ch in tiles) count[ch - 'A']++
        return dfs(count)
    }

    private fun dfs(count: IntArray): Int {
        var total = 0
        for (i in 0 until 26) {
            if (count[i] == 0) continue
            count[i]--
            total += 1 + dfs(count)
            count[i]++
        }
        return total
    }
}
