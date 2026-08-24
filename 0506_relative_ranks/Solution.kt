// LeetCode 0506 - Relative Ranks
// https://leetcode.com/problems/relative-ranks/

class Solution {
    fun findRelativeRanks(score: IntArray): Array<String> {
        val medals = mapOf(
            1 to "Gold Medal",
            2 to "Silver Medal",
            3 to "Bronze Medal",
        )
        val order = score.indices.sortedByDescending { score[it] }
        val result = Array(score.size) { "" }
        order.forEachIndexed { rank, index ->
            result[index] = medals.getOrDefault(rank + 1, (rank + 1).toString())
        }
        return result
    }
}
