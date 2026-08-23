// LeetCode 3796 - Find Maximum Value in a Constrained Sequence
// https://leetcode.com/problems/find-maximum-value-in-a-constrained-sequence/

class Solution {
    public int maxValue(int n, int[][] restrictions, int[] diff) {
        final int INF = Integer.MAX_VALUE / 4;
        int[] bound = new int[n];
        for (int i = 0; i < n; i++) bound[i] = INF;
        bound[0] = 0;
        for (var r : restrictions) bound[r[0]] = r[1];
        for (int i = 1; i < n; i++) bound[i] = Math.min(bound[i], bound[i - 1] + diff[i - 1]);
        for (int i = n - 2; i >= 0; i--) bound[i] = Math.min(bound[i], bound[i + 1] + diff[i]);
        int ans = bound[0];
        for (int i = 1; i < n; i++) ans = Math.max(ans, bound[i]);
        return ans;
    }
}
