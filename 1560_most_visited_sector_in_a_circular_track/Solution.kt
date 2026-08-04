// LeetCode 1560 - Most Visited Sector in a Circular Track
// https://leetcode.com/problems/most-visited-sector-in-a-circular-track/

class Solution {
    fun mostVisited(n: Int, rounds: IntArray): List<Int> {
        val start = rounds[0]
        val end = rounds[rounds.size - 1]
        val ans = mutableListOf<Int>()
        if (start <= end) {
            for (i in start..end) ans.add(i)
        } else {
            for (i in 1..end) ans.add(i)
            for (i in start..n) ans.add(i)
        }
        return ans
    }
}
