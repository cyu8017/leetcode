// LeetCode 2121 - Intervals Between Identical Elements
// https://leetcode.com/problems/intervals-between-identical-elements/

public class Solution {
    public long[] GetDistances(int[] arr) {
        int n = arr.Length;
        var pos = new Dictionary<int, List<int>>();
        for (int i = 0; i < n; i++) {
            if (!pos.ContainsKey(arr[i])) pos[arr[i]] = new List<int>();
            pos[arr[i]].Add(i);
        }
        long[] ans = new long[n];
        foreach (var idxs in pos.Values) {
            int m = idxs.Count;
            long[] pref = new long[m + 1];
            for (int i = 0; i < m; i++) pref[i + 1] = pref[i] + idxs[i];
            for (int i = 0; i < m; i++) {
                long left = 1L * i * idxs[i] - pref[i];
                long right = (pref[m] - pref[i + 1]) - 1L * (m - i - 1) * idxs[i];
                ans[idxs[i]] = left + right;
            }
        }
        return ans;
    }
}
