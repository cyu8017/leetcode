// LeetCode 3297 - Count Substrings That Can Be Rearranged to Contain a String I
// https://leetcode.com/problems/count-substrings-that-can-be-rearranged-to-contain-a-string-i/

class Solution {
    public long validSubstringCount(String word1, String word2) {
        int[] need = new int[26];
        int required = 0;
        for (char c : word2.toCharArray()) {
            if (need[c - 'a'] == 0) required++;
            need[c - 'a']++;
        }
        int[] have = new int[26];
        int formed = 0;
        long ans = 0;
        int l = 0;
        for (int r = 0; r < word1.length(); r++) {
            int c = word1.charAt(r) - 'a';
            have[c]++;
            if (have[c] == need[c] && need[c] > 0) formed++;
            while (formed == required && l <= r) {
                ans += word1.length() - r;
                int c2 = word1.charAt(l) - 'a';
                if (have[c2] == need[c2] && need[c2] > 0) formed--;
                have[c2]--;
                l++;
            }
        }
        return ans;
    }
}
