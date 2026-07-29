// LeetCode 1065 - Index Pairs of a String
// https://leetcode.com/problems/index-pairs-of-a-string/

class Solution {
    fun indexPairs(text: String, words: Array<String>): Array<IntArray> {
        val wordSet = words.toSet()
        val ans = mutableListOf<IntArray>()
        val n = text.length
        for (i in 0 until n) {
            for (j in i until n) {
                if (text.substring(i, j + 1) in wordSet) {
                    ans.add(intArrayOf(i, j))
                }
            }
        }
        return ans.toTypedArray()
    }
}
