// LeetCode 1733 - Minimum Number of People to Teach
// https://leetcode.com/problems/minimum-number-of-people-to-teach/

class Solution {
    fun minimumTeachings(n: Int, languages: Array<IntArray>, friendships: Array<IntArray>): Int {
        val users = languages.size
        val knows = Array(users) { BooleanArray(n + 1) }
        for (user in 0 until users) {
            for (lang in languages[user]) {
                knows[user][lang] = true
            }
        }
        val need = HashSet<Int>()
        for (friendship in friendships) {
            val u = friendship[0] - 1
            val v = friendship[1] - 1
            val shares = languages[u].any { lang -> knows[v][lang] }
            if (!shares) {
                need.add(u)
                need.add(v)
            }
        }
        if (need.isEmpty()) {
            return 0
        }
        var best = Int.MAX_VALUE
        for (lang in 1..n) {
            val teach = need.count { user -> !knows[user][lang] }
            best = minOf(best, teach)
        }
        return best
    }
}
