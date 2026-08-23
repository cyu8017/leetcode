// LeetCode 2121 - Intervals Between Identical Elements
// https://leetcode.com/problems/intervals-between-identical-elements/

import java.util.*;

class Solution {
    public long[] getDistances(int[] arr) {
        int n = arr.length;
        Map<Integer, List<Integer>> pos = new HashMap<>();
        for (int i = 0; i < n; i++) pos.computeIfAbsent(arr[i], k -> new ArrayList<>()).add(i);
        long[] ans = new long[n];
        for (List<Integer> idxs : pos.values()) {
            int m = idxs.size();
            long[] pref = new long[m + 1];
            for (int i = 0; i < m; i++) pref[i + 1] = pref[i] + idxs.get(i);
            for (int i = 0; i < m; i++) {
                long left = 1L * i * idxs.get(i) - pref[i];
                long right = (pref[m] - pref[i + 1]) - 1L * (m - i - 1) * idxs.get(i);
                ans[idxs.get(i)] = left + right;
            }
        }
        return ans;
    }
}
