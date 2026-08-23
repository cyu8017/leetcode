// LeetCode 3460 - Longest Common Prefix After at Most One Removal
// https://leetcode.com/problems/longest-common-prefix-after-at-most-one-removal/

public class Solution {
    public int LongestCommonPrefix(string s, string t) {
        int i = 0, j = 0;
        bool removed = false;
        while (i < s.Length && j < t.Length) {
            if (s[i] == t[j]) {
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
