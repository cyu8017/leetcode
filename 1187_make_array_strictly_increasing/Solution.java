// LeetCode 1187 - Make Array Strictly Increasing
// https://leetcode.com/problems/make-array-strictly-increasing/

import java.util.*;

class Solution {
    public int makeArrayIncreasing(int[] arr1, int[] arr2) {
        TreeSet<Integer> set = new TreeSet<>();
        for (int x : arr2) set.add(x);
        Integer[] sorted = set.toArray(new Integer[0]);
        Map<Integer, Integer> dp = new HashMap<>();
        dp.put(-1, 0);
        for (int num : arr1) {
            Map<Integer, Integer> next = new HashMap<>();
            for (Map.Entry<Integer, Integer> e : dp.entrySet()) {
                int prev = e.getKey(), ops = e.getValue();
                if (num > prev) next.merge(num, ops, Math::min);
                int idx = upperBound(sorted, prev);
                if (idx < sorted.length) {
                    int chosen = sorted[idx];
                    next.merge(chosen, ops + 1, Math::min);
                }
            }
            dp = next;
            if (dp.isEmpty()) return -1;
        }
        int ans = Integer.MAX_VALUE;
        for (int v : dp.values()) ans = Math.min(ans, v);
        return ans;
    }
    private int upperBound(Integer[] a, int target) {
        int lo = 0, hi = a.length;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (a[mid] <= target) lo = mid + 1; else hi = mid;
        }
        return lo;
    }
}
