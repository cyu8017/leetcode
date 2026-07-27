// LeetCode 1678 - Goal Parser Interpretation
// https://leetcode.com/problems/goal-parser-interpretation/

class Solution {
    public String interpret(String command) {
        return command.replace("()", "o").replace("(al)", "al");
    }
}
