// LeetCode 3572 - Maximize Y-Sum by Picking a Triplet of Distinct X-Values
// https://leetcode.com/problems/maximize-ysum-by-picking-a-triplet-of-distinct-xvalues/

import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

class Solution {
    public int maxSumDistinctTriplet(int[] x, int[] y) {
        int n = x.length;
        int[][] arr = new int[n][2];
        for (int i = 0; i < n; i++) arr[i] = new int[] {x[i], y[i]};
        Arrays.sort(arr, (a, b) -> Integer.compare(b[1], a[1]));
        int ans = 0;
        Set<Integer> vis = new HashSet<>();
        for (int i = 0; i < n; i++) {
            int a = arr[i][0], b = arr[i][1];
            if (!vis.contains(a)) {
                vis.add(a);
                ans += b;
                if (vis.size() == 3) return ans;
            }
        }
        return -1;
    }
}
