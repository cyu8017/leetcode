// LeetCode 2070 - Most Beautiful Item for Each Query
// https://leetcode.com/problems/most-beautiful-item-for-each-query/

using System;

public class Solution {
    public int[] MaximumBeauty(int[][] items, int[] queries) {
        Array.Sort(items, (a, b) => a[0].CompareTo(b[0]));
        int maxB = 0;
        foreach (var it in items) {
            maxB = Math.Max(maxB, it[1]);
            it[1] = maxB;
        }
        int[] ans = new int[queries.Length];
        for (int i = 0; i < queries.Length; i++) {
            int lo = 0, hi = items.Length;
            while (lo < hi) {
                int mid = (lo + hi) / 2;
                if (items[mid][0] <= queries[i]) lo = mid + 1;
                else hi = mid;
            }
            ans[i] = lo == 0 ? 0 : items[lo - 1][1];
        }
        return ans;
    }
}
