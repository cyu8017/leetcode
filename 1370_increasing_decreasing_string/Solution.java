// LeetCode 1370 - Increasing Decreasing String
// https://leetcode.com/problems/increasing-decreasing-string/

class Solution {
    public String sortString(String s) {
        int[] c = new int[26];
        for (char ch : s.toCharArray()) c[ch - 'a']++;
        StringBuilder out = new StringBuilder();
        while (out.length() < s.length()) {
            for (int i = 0; i < 26; i++) {
                if (c[i] > 0) {
                    out.append((char) ('a' + i));
                    c[i]--;
                }
            }
            for (int i = 25; i >= 0; i--) {
                if (c[i] > 0) {
                    out.append((char) ('a' + i));
                    c[i]--;
                }
            }
        }
        return out.toString();
    }
}
