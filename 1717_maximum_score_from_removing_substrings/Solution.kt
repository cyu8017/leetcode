// LeetCode 1717 - Maximum Score From Removing Substrings
// https://leetcode.com/problems/maximum-score-from-removing-substrings/

class Solution {
    fun maximumGain(s: String, x: Int, y: Int): Int {
        fun remove(text: String, open: Char, close: Char, score: Int): Pair<String, Int> {
            val stack = StringBuilder()
            var gained = 0
            for (ch in text) {
                if (stack.isNotEmpty() && stack.last() == open && ch == close) {
                    stack.deleteCharAt(stack.length - 1)
                    gained += score
                } else {
                    stack.append(ch)
                }
            }
            return Pair(stack.toString(), gained)
        }

        return if (x >= y) {
            val (rest, first) = remove(s, 'a', 'b', x)
            val (_, second) = remove(rest, 'b', 'a', y)
            first + second
        } else {
            val (rest, first) = remove(s, 'b', 'a', y)
            val (_, second) = remove(rest, 'a', 'b', x)
            first + second
        }
    }
}
