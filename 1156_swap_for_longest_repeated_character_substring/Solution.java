// LeetCode 1156 - Swap For Longest Repeated Character Substring
// https://leetcode.com/problems/swap-for-longest-repeated-character-substring/

class Solution {
    public int maxRepOpt1(String text) {
        int[] count = new int[26];
        for (char c : text.toCharArray()) count[c - 'a']++;
        int n = text.length(), ans = 0, i = 0;
        while (i < n) {
            int j = i;
            while (j < n && text.charAt(j) == text.charAt(i)) j++;
            int length = j - i;
            int k = j + 1;
            while (k < n && text.charAt(k) == text.charAt(i)) k++;
            int length2 = j < n ? k - j - 1 : 0;
            ans = Math.max(ans, Math.min(length + length2 + 1, count[text.charAt(i) - 'a']));
            i = j;
        }
        return ans;
    }
}
