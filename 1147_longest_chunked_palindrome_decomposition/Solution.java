// LeetCode 1147 - Longest Chunked Palindrome Decomposition
// https://leetcode.com/problems/longest-chunked-palindrome-decomposition/

class Solution {
    public int longestDecomposition(String text) {
        int n = text.length(), ans = 0, i = 0;
        while (i < n - i) {
            boolean found = false;
            for (int length = 1; length <= (n - 2 * i) / 2; length++) {
                if (text.substring(i, i + length).equals(text.substring(n - i - length, n - i))) {
                    ans += 2;
                    i += length;
                    found = true;
                    break;
                }
            }
            if (!found) {
                ans++;
                break;
            }
        }
        return ans;
    }
}
