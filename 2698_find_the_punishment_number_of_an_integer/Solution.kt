// LeetCode 2698 - Find the Punishment Number of an Integer
// https://leetcode.com/problems/find-the-punishment-number-of-an-integer/

class Solution {
    fun punishmentNumber(n: Int): Int {
        var ans = 0
        for (i in 1..n) {
            val sq = i * i
            if (can(sq, i)) ans += sq
        }
        return ans
    }

    private fun can(sq: Int, target: Int): Boolean = dfs(sq.toString(), 0, 0, target)

    private fun dfs(s: String, i: Int, sum: Int, target: Int): Boolean {
        val m = s.length
        if (i == m) return sum == target
        var cur = 0
        for (j in i until m) {
            cur = cur * 10 + (s[j] - '0')
            if (sum + cur > target) break
            if (dfs(s, j + 1, sum + cur, target)) return true
        }
        return false
    }
}
