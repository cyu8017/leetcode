// LeetCode 2955 - Number of Same-End Substrings
// https://leetcode.com/problems/number-of-same-end-substrings/

public class Solution {
    public int[] SameEndSubstringCount(string s, int[][] queries) {
        int n = s.Length;
        int[][] pref = new int[n + 1][];
        pref[0] = new int[26];
        for (int i = 0; i < n; i++) {
            pref[i + 1] = (int[])pref[i].Clone();
            pref[i + 1][s[i] - 'a']++;
        }
        int[] ans = new int[queries.Length];
        for (int qi = 0; qi < queries.Length; qi++) {
            int l = queries[qi][0], r = queries[qi][1], total = 0;
            for (int c = 0; c < 26; c++) {
                int cnt = pref[r + 1][c] - pref[l][c];
                total += cnt * (cnt + 1) / 2;
            }
            ans[qi] = total;
        }
        return ans;
    }
}
