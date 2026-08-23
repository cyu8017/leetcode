// LeetCode 1717 - Maximum Score From Removing Substrings
// https://leetcode.com/problems/maximum-score-from-removing-substrings/

public class Solution {
    public int MaximumGain(string s, int x, int y) {
        int first;
        int second;
        if (x >= y) {
            (string rest, first) = Remove(s, 'a', 'b', x);
            (_, second) = Remove(rest, 'b', 'a', y);
        } else {
            (string rest, first) = Remove(s, 'b', 'a', y);
            (_, second) = Remove(rest, 'a', 'b', x);
        }
        return first + second;
    }

    private (string, int) Remove(string text, char open, char close, int score) {
        var stack = new StringBuilder();
        int gained = 0;
        foreach (char ch in text) {
            if (stack.Length > 0 && stack[stack.Length - 1] == open && ch == close) {
                stack.Length--;
                gained += score;
            } else {
                stack.Append(ch);
            }
        }
        return (stack.ToString(), gained);
    }
}
