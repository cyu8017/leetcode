// LeetCode 0072 - Edit Distance
// https://leetcode.com/problems/edit-distance/

class Solution {
    fun minDistance(word1: String, word2: String): Int {
        val m = word1.length
        val n = word2.length
        var prev = IntArray(n + 1) { it }
        var curr = IntArray(n + 1)

        for (i in 1..m) {
            curr[0] = i
            for (j in 1..n) {
                curr[j] = if (word1[i - 1] == word2[j - 1]) {
                    prev[j - 1]
                } else {
                    1 + minOf(prev[j], curr[j - 1], prev[j - 1])
                }
            }
            val tmp = prev
            prev = curr
            curr = tmp
        }

        return prev[n]
    }
}
