// LeetCode 0459 - Repeated Substring Pattern
// https://leetcode.com/problems/repeated-substring-pattern/

public class Solution {
    public bool RepeatedSubstringPattern(string s) {
        string doubled = s + s;
        return doubled.Substring(1, s.Length * 2 - 2).Contains(s);
    }
}
