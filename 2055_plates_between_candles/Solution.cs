// LeetCode 2055 - Plates Between Candles
// https://leetcode.com/problems/plates-between-candles/

public class Solution {
    public int[] PlatesBetweenCandles(string s, int[][] queries) {
        int n = s.Length;
        int[] pref = new int[n + 1], left = new int[n], right = new int[n];
        int last = -1;
        for (int i = 0; i < n; i++) {
            pref[i + 1] = pref[i] + (s[i] == '*' ? 1 : 0);
            if (s[i] == '|') last = i;
            left[i] = last;
        }
        last = -1;
        for (int i = n - 1; i >= 0; i--) {
            if (s[i] == '|') last = i;
            right[i] = last;
        }
        int[] ans = new int[queries.Length];
        for (int i = 0; i < queries.Length; i++) {
            int l = right[queries[i][0]], r = left[queries[i][1]];
            if (l != -1 && r != -1 && l < r) ans[i] = pref[r] - pref[l];
        }
        return ans;
    }
}
