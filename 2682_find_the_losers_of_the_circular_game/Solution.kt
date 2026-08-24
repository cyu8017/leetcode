// LeetCode 2682 - Find the Losers of the Circular Game
// https://leetcode.com/problems/find-the-losers-of-the-circular-game/

class Solution {
    fun circularGameLosers(n: Int, k: Int): IntArray {
        val seen = BooleanArray(n + 1)
        var cur = 1
        var step = 1
        while (!seen[cur]) {
            seen[cur] = true
            cur = (cur - 1 + step * k) % n + 1
            step++
        }
        val ans = ArrayList<Int>()
        for (i in 1..n) if (!seen[i]) ans.add(i)
        return ans.toIntArray()
    }
}
