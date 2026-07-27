// LeetCode 1678 - Goal Parser Interpretation
// https://leetcode.com/problems/goal-parser-interpretation/

class Solution {
    fun interpret(command: String): String {
        return command.replace("()", "o").replace("(al)", "al")
    }
}
