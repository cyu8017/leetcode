// LeetCode 1147 - Longest Chunked Palindrome Decomposition
// https://leetcode.com/problems/longest-chunked-palindrome-decomposition/

public class Solution {
    public int LongestDecomposition(string text) {
        int n = text.Length, ans = 0, i = 0;
        while (i < n - i) {
            bool found = false;
            for (int length = 1; length <= (n - 2 * i) / 2; length++) {
                if (text.Substring(i, length) == text.Substring(n - i - length, length)) {
                    ans += 2;
                    i += length;
                    found = true;
                    break;
                }
            }
            if (!found) { ans += 1; break; }
        }
        return ans;
    }
}
