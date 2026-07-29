// LeetCode 1078 - Occurrences After Bigram
// https://leetcode.com/problems/occurrences-after-bigram/

class Solution {
    fun findOcurrences(text: String, first: String, second: String): Array<String> {
        val words = text.split(Regex("\\s+"))
        val ans = mutableListOf<String>()
        for (i in 0 until words.size - 2) {
            if (words[i] == first && words[i + 1] == second) {
                ans.add(words[i + 2])
            }
        }
        return ans.toTypedArray()
    }
}
