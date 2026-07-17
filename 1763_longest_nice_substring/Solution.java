// LeetCode 1763 - Longest Nice Substring
// https://leetcode.com/problems/longest-nice-substring/

class Solution {
    public String longestNiceSubstring(String s) {
        int bestStart = 0;
        int bestLen = 0;
        for (int i = 0; i < s.length(); i++) {
            int lower = 0;
            int upper = 0;
            for (int j = i; j < s.length(); j++) {
                char c = s.charAt(j);
                if (Character.isLowerCase(c)) {
                    lower |= 1 << (c - 'a');
                } else {
                    upper |= 1 << (c - 'A');
                }
                if (lower == upper && j - i + 1 > bestLen) {
                    bestStart = i;
                    bestLen = j - i + 1;
                }
            }
        }
        return s.substring(bestStart, bestStart + bestLen);
    }
}
