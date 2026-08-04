// LeetCode 1324 - Print Words Vertically
// https://leetcode.com/problems/print-words-vertically/

class Solution {
    fun printVertically(s: String): List<String> {
        val words = s.split(" ")
        val maxLen = words.maxOf { it.length }
        return (0 until maxLen).map { i ->
            words.joinToString("") { word -> if (i < word.length) word[i].toString() else " " }.trimEnd()
        }
    }
}
