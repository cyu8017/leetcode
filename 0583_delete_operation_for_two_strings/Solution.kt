// LeetCode 0583 - Delete Operation for Two Strings
// https://leetcode.com/problems/delete-operation-for-two-strings/


class Solution {
    fun minDistance(word1: String, word2: String): Int {
        val m = word1.length
        val n = word2.length
        var prev = IntArray(n + 1)
        var curr = IntArray(n + 1)
        for (i in 1..m) {
            for (j in 1..n) {
                curr[j] = if (word1[i - 1] == word2[j - 1]) prev[j - 1] + 1 else maxOf(prev[j], curr[j - 1])
            }
            val tmp = prev
            prev = curr
            curr = tmp
            curr.fill(0)
        }
        return m + n - 2 * prev[n]
    }
}
