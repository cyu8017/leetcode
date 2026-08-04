// LeetCode 1930 - Unique Length-3 Palindromic Subsequences
// https://leetcode.com/problems/unique-length-3-palindromic-subsequences/

import java.util.*;

class Solution {
    public int countPalindromicSubsequence(String s) {
        int[] first = new int[26], last = new int[26];
        Arrays.fill(first, -1);
        for (int i = 0; i < s.length(); i++) {
            int c = s.charAt(i) - 'a';
            if (first[c] == -1) first[c] = i;
            last[c] = i;
        }
        int ans = 0;
        for (int c = 0; c < 26; c++) {
            if (first[c] != -1 && last[c] - first[c] > 1) {
                Set<Character> mid = new HashSet<>();
                for (int i = first[c] + 1; i < last[c]; i++) mid.add(s.charAt(i));
                ans += mid.size();
            }
        }
        return ans;
    }
}
