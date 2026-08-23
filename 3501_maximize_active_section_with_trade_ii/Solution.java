// LeetCode 3501 - Maximize Active Section with Trade II
// https://leetcode.com/problems/maximize-active-section-with-trade-ii/

class Solution {
    public int[] maxActiveSectionsAfterTrade(String s, int[][] queries) {
        int ones = 0;
        for (char c : s.toCharArray()) if (c == '1') ones++;
        int[] ans = new int[queries.length];
        for (int i = 0; i < ans.length; i++) ans[i] = ones;
        return ans;
    }
}
