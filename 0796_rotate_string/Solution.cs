// LeetCode 0796 - Rotate String
// https://leetcode.com/problems/rotate-string/

public class Solution {
    public bool RotateString(string s, string goal) {
        return s.Length == goal.Length && (s + s).Contains(goal);
    }
}
