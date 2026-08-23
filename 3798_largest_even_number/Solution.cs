// LeetCode 3798 - Largest Even Number
// https://leetcode.com/problems/largest-even-number/

public class Solution {
    public string LargestEven(string s) {
        while (s.Length > 0 && s[s.Length - 1] == '1') s = s.Substring(0, s.Length - 1);
        return s;
    }
}
