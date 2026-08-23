// LeetCode 2030 - Smallest K-Length Subsequence With Occurrences of a Letter
// https://leetcode.com/problems/smallest-k-length-subsequence-with-occurrences-of-a-letter/

class Solution {
    public String smallestSubsequence(String s, int k, char letter, int repetition) {
        int n = s.length(), remainLetter = 0;
        for (char c : s.toCharArray()) if (c == letter) remainLetter++;
        StringBuilder stack = new StringBuilder();
        int inStackLetter = 0;
        for (int i = 0; i < n; i++) {
            char ch = s.charAt(i);
            while (stack.length() > 0 && ch < stack.charAt(stack.length() - 1) && stack.length() + n - i > k) {
                char top = stack.charAt(stack.length() - 1);
                if (top == letter) {
                    if (inStackLetter + remainLetter - 1 < repetition) break;
                    inStackLetter--;
                }
                stack.setLength(stack.length() - 1);
            }
            if (stack.length() < k) {
                if (ch == letter) { stack.append(ch); inStackLetter++; }
                else if (k - stack.length() > repetition - inStackLetter) stack.append(ch);
            }
            if (ch == letter) remainLetter--;
        }
        return stack.toString();
    }
}
