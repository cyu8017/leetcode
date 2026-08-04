// LeetCode 1528 - Shuffle String
// https://leetcode.com/problems/shuffle-string/

class Solution {
    fun restoreString(s: String, indices: IntArray): String {
        val answer = CharArray(s.length)
        for (i in s.indices) {
            answer[indices[i]] = s[i]
        }
        return String(answer)
    }
}
