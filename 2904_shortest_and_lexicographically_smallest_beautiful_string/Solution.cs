// LeetCode 2904 - Shortest and Lexicographically Smallest Beautiful String
// https://leetcode.com/problems/shortest-and-lexicographically-smallest-beautiful-string/

public class Solution {
    public string ShortestBeautifulSubstring(string s, int k) {
        string ans = "";
        int n = s.Length;
        for (int i = 0; i < n; i++) {
            int ones = 0;
            for (int j = i; j < n; j++) {
                if (s[j] == '1') ones++;
                if (ones == k) {
                    string cand = s.Substring(i, j - i + 1);
                    if (ans.Length == 0 || cand.Length < ans.Length || (cand.Length == ans.Length && string.CompareOrdinal(cand, ans) < 0))
                        ans = cand;
                    break;
                }
                if (ones > k) break;
            }
        }
        return ans;
    }
}
