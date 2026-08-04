// LeetCode 1593 - Split a String Into the Max Number of Unique Substrings
// https://leetcode.com/problems/split-a-string-into-the-max-number-of-unique-substrings/

class Solution {
    fun maxUniqueSplit(s: String): Int {
        val used = HashSet<String>()
        val answer = intArrayOf(0)
        dfs(s, 0, used, answer)
        return answer[0]
    }

    private fun dfs(s: String, i: Int, used: HashSet<String>, answer: IntArray) {
        if (used.size + s.length - i <= answer[0]) return
        if (i == s.length) {
            answer[0] = maxOf(answer[0], used.size)
            return
        }
        for (j in i + 1..s.length) {
            val part = s.substring(i, j)
            if (part !in used) {
                used.add(part)
                dfs(s, j, used, answer)
                used.remove(part)
            }
        }
    }
}
