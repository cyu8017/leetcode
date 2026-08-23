// LeetCode 0583 - Delete Operation for Two Strings
// https://leetcode.com/problems/delete-operation-for-two-strings/

public class Solution {
    public int MinDistance(string word1, string word2) {
        int m = word1.Length, n = word2.Length;
        int[] prev = new int[n + 1];
        int[] curr = new int[n + 1];
        for (int i = 1; i <= m; ++i) {
            for (int j = 1; j <= n; ++j) {
                if (word1[i - 1] == word2[j - 1]) curr[j] = prev[j - 1] + 1;
                else curr[j] = System.Math.Max(prev[j], curr[j - 1]);
            }
            (prev, curr) = (curr, prev);
            System.Array.Fill(curr, 0);
        }
        return m + n - 2 * prev[n];
    }
}
