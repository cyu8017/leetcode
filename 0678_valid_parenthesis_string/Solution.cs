// LeetCode 0678 - Valid Parenthesis String
// https://leetcode.com/problems/valid-parenthesis-string/

public class Solution {
    public bool CheckValidString(string s) {
        int lo = 0, hi = 0;
        foreach (char ch in s) {
            if (ch == '(') {
                ++lo;
                ++hi;
            } else if (ch == ')') {
                lo = System.Math.Max(lo - 1, 0);
                --hi;
                if (hi < 0) return false;
            } else {
                lo = System.Math.Max(lo - 1, 0);
                ++hi;
            }
        }
        return lo == 0;
    }
}
