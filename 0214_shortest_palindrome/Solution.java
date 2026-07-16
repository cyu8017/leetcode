// LeetCode 0214 - Shortest Palindrome
// https://leetcode.com/problems/shortest-palindrome/

class Solution {
    public String shortestPalindrome(String s) {
        if (s.isEmpty()) {
            return "";
        }
        String reversed = new StringBuilder(s).reverse().toString();
        String combined = s + "#" + reversed;
        int[] pi = new int[combined.length()];
        int lps = 0;
        for (int i = 1; i < combined.length(); i++) {
            while (lps > 0 && combined.charAt(i) != combined.charAt(lps)) {
                lps = pi[lps - 1];
            }
            if (combined.charAt(i) == combined.charAt(lps)) {
                lps++;
            }
            pi[i] = lps;
        }
        int prefixLen = pi[combined.length() - 1];
        return reversed.substring(0, s.length() - prefixLen) + s;
    }
}
