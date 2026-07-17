// LeetCode 1758 - Minimum Changes To Make Alternating Binary String
// https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/

public class Solution {
    public int MinOperations(string s) {
        int alt1 = 0;
        for (int i = 0; i < s.Length; i++) {
            char expected = (i & 1) == 0 ? '0' : '1';
            if (s[i] != expected) {
                alt1++;
            }
        }
        return System.Math.Min(alt1, s.Length - alt1);
    }
}
