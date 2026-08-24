// LeetCode 0422 - Valid Word Square
// https://leetcode.com/problems/valid-word-square/

class Solution {
    fun validWordSquare(words: Array<String>): Boolean {
        for ((row, word) in words.withIndex()) {
            for ((col, char) in word.withIndex()) {
                if (col >= words.size || row >= words[col].length || words[col][row] != char) {
                    return false
                }
            }
        }
        return true
    }
}
