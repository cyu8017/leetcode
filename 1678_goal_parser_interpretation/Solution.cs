// LeetCode 1678 - Goal Parser Interpretation
// https://leetcode.com/problems/goal-parser-interpretation/

public class Solution {
    public string Interpret(string command) {
        return command.Replace("()", "o").Replace("(al)", "al");
    }
}
