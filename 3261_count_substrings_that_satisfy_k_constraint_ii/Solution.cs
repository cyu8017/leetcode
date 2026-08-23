// LeetCode 3261 - Count Substrings That Satisfy K-Constraint II
// https://leetcode.com/problems/count-substrings-that-satisfy-k-constraint-ii/

public class Solution {
    public long[] CountKConstraintSubstrings(string s, int k, int[][] queries) {
        int n = s.Length;
        int[] leftMost = new int[n];
        int z = 0, o = 0, L = 0;
        for (int R = 0; R < n; R++) {
            if (s[R] == '0') z++; else o++;
            while (z > k && o > k) {
                if (s[L] == '0') z--; else o--;
                L++;
            }
            leftMost[R] = L;
        }
        long[] pref = new long[n + 1];
        for (int i = 0; i < n; i++) pref[i + 1] = pref[i] + (i - leftMost[i] + 1);
        long[] ans = new long[queries.Length];
        for (int qi = 0; qi < queries.Length; qi++) {
            int l = queries[qi][0], r = queries[qi][1];
            int lo = l, hi = r + 1;
            while (lo < hi) {
                int mid = (lo + hi) / 2;
                if (leftMost[mid] < l) lo = mid + 1;
                else hi = mid;
            }
            long res = 0;
            if (lo > l) {
                long m = lo - l;
                res += m * (m + 1) / 2;
            }
            if (lo <= r) res += pref[r + 1] - pref[lo];
            ans[qi] = res;
        }
        return ans;
    }
}
