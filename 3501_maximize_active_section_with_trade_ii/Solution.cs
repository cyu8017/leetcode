// LeetCode 3501 - Maximize Active Section with Trade II
// https://leetcode.com/problems/maximize-active-section-with-trade-ii/

public class Solution {
    public int[] MaxActiveSectionsAfterTrade(string s, int[][] queries) {
        int ones = 0;
        foreach (char c in s) if (c == '1') ones++;
        int[] ans = new int[queries.Length];
        for (int i = 0; i < ans.Length; i++) ans[i] = ones;
        return ans;
    }
}
