// LeetCode 1016 - Binary String With Substrings Representing 1 To N
// https://leetcode.com/problems/binary-string-with-substrings-representing-1-to-n/

public class Solution {
    public bool QueryString(string s, int n) {
        for (int i = n; i > n / 2; i--) {
            string bin = Convert.ToString(i, 2);
            if (!s.Contains(bin)) return false;
        }
        return true;
    }
}
