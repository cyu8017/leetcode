// LeetCode 1583 - Count Unhappy Friends
// https://leetcode.com/problems/count-unhappy-friends/

class Solution {
    fun unhappyFriends(n: Int, preferences: Array<IntArray>, pairs: Array<IntArray>): Int {
        val rank = Array(n) { IntArray(n) }
        for (i in 0 until n) {
            for (j in 0 until n - 1) {
                rank[i][preferences[i][j]] = j
            }
        }
        val partner = IntArray(n)
        for (p in pairs) {
            partner[p[0]] = p[1]
            partner[p[1]] = p[0]
        }
        var unhappy = 0
        for (x in 0 until n) {
            val y = partner[x]
            for (k in 0 until rank[x][y]) {
                val u = preferences[x][k]
                if (rank[u][x] < rank[u][partner[u]]) {
                    unhappy++
                    break
                }
            }
        }
        return unhappy
    }
}
