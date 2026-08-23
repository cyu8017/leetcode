// LeetCode 1758 - Minimum Changes To Make Alternating Binary String
// https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/

class Solution {
    public int minOperations(String s) {
        int alt1 = 0;
        for (int i = 0; i < s.length(); i++) {
            char expected = (i & 1) == 0 ? '0' : '1';
            if (s.charAt(i) != expected) {
                alt1++;
            }
        }
        return Math.min(alt1, s.length() - alt1);
    }
}
