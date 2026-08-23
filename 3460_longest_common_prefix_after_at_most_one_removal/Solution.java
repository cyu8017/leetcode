// LeetCode 3460 - Longest Common Prefix After at Most One Removal
// https://leetcode.com/problems/longest-common-prefix-after-at-most-one-removal/

class Solution {
    public int longestCommonPrefix(String s, String t) {
        int i = 0, j = 0;
        boolean removed = false;
        while (i < s.length() && j < t.length()) {
            if (s.charAt(i) == t.charAt(j)) {
                i++;
                j++;
                continue;
            }
            if (removed) break;
            removed = true;
            i++;
        }
        return j;
    }
}
