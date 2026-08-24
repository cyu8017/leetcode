// LeetCode 3175 - Find The First Player to win K Games in a Row
// https://leetcode.com/problems/find-the-first-player-to-win-k-games-in-a-row/

class Solution {
    fun findWinningPlayer(skills: IntArray, k: Int): Int {
        var n = skills.size
        k = minOf(k, n - 1)
        var i = 0
        var cnt = 0
        for (j in 1 until n) {
            if (skills[i] < skills[j]) { i = j; cnt = 1; }
            else cnt++
            if (cnt == k) break
        }
        return i
    }
}
