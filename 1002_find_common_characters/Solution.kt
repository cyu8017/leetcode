// LeetCode 1002 - Find Common Characters
// https://leetcode.com/problems/find-common-characters/

class Solution {
    fun commonChars(words: Array<String>): List<String> {
        val common = IntArray(26) { Int.MAX_VALUE }
        for (w in words) {
            val cnt = IntArray(26)
            for (ch in w) cnt[ch - 'a']++
            for (i in 0 until 26) common[i] = minOf(common[i], cnt[i])
        }
        val ans = mutableListOf<String>()
        for (i in 0 until 26) {
            repeat(common[i]) { ans.add(('a' + i).toString()) }
        }
        return ans
    }
}
