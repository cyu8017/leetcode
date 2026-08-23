// LeetCode 2070 - Most Beautiful Item for Each Query
// https://leetcode.com/problems/most-beautiful-item-for-each-query/

import java.util.*;

class Solution {
    public int[] maximumBeauty(int[][] items, int[] queries) {
        Arrays.sort(items, (a, b) -> Integer.compare(a[0], b[0]));
        int maxB = 0;
        for (int[] it : items) {
            maxB = Math.max(maxB, it[1]);
            it[1] = maxB;
        }
        int[] ans = new int[queries.length];
        for (int i = 0; i < queries.length; i++) {
            int lo = 0, hi = items.length;
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
