// LeetCode 3407 - Substring Matching Pattern
// https://leetcode.com/problems/substring-matching-pattern/

public class Solution {
    public bool HasMatch(string s, string p) {
        int i = p.IndexOf('*');
        string left = p.Substring(0, i);
        string right = p.Substring(i + 1);
        int li = s.IndexOf(left, System.StringComparison.Ordinal);
        if (li < 0) return false;
        return s.IndexOf(right, li + left.Length, System.StringComparison.Ordinal) >= 0;
    }
}
