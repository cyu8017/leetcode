// LeetCode 1366 - Rank Teams by Votes
// https://leetcode.com/problems/rank-teams-by-votes/

class Solution {
    fun rankTeams(votes: Array<String>): String {
        val m = votes[0].length
        val count = mutableMapOf<Char, IntArray>()
        for (c in votes[0]) count[c] = IntArray(m)
        for (v in votes) {
            for (i in v.indices) count[v[i]]!![i]++
        }
        return count.keys.sortedWith { a, b ->
            val ca = count[a]!!
            val cb = count[b]!!
            for (i in 0 until m) {
                if (ca[i] != cb[i]) return@sortedWith cb[i] - ca[i]
            }
            a - b
        }.joinToString("")
    }
}
