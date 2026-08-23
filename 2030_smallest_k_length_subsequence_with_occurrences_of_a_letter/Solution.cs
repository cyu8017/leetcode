// LeetCode 2030 - Smallest K-Length Subsequence With Occurrences of a Letter
// https://leetcode.com/problems/smallest-k-length-subsequence-with-occurrences-of-a-letter/

using System.Text;

public class Solution {
    public string SmallestSubsequence(string s, int k, char letter, int repetition) {
        int n = s.Length, remainLetter = 0;
        foreach (char c in s) if (c == letter) remainLetter++;
        var stack = new StringBuilder();
        int inStackLetter = 0;
        for (int i = 0; i < n; i++) {
            char ch = s[i];
            while (stack.Length > 0 && ch < stack[stack.Length - 1] && stack.Length + n - i > k) {
                char top = stack[stack.Length - 1];
                if (top == letter) {
                    if (inStackLetter + remainLetter - 1 < repetition) break;
                    inStackLetter--;
                }
                stack.Length--;
            }
            if (stack.Length < k) {
                if (ch == letter) { stack.Append(ch); inStackLetter++; }
                else if (k - stack.Length > repetition - inStackLetter) stack.Append(ch);
            }
            if (ch == letter) remainLetter--;
        }
        return stack.ToString();
    }
}
