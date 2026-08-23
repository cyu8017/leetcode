// LeetCode 2931 - Maximum Spending After Buying Items
// https://leetcode.com/problems/maximum-spending-after-buying-items/

public class Solution {
    public long MaxSpending(int[][] values) {
        int m = values.Length, n = values[0].Length;
        int[] idx = new int[m];
        for (int i = 0; i < m; i++) idx[i] = n - 1;
        long ans = 0, day = 1;
        int total = m * n;
        for (int t = 0; t < total; t++) {
            int bestI = -1;
            long bestV = 1L << 60;
            for (int i = 0; i < m; i++) {
                if (idx[i] >= 0 && values[i][idx[i]] < bestV) {
                    bestV = values[i][idx[i]];
                    bestI = i;
                }
            }
            ans += 1L * bestV * day;
            idx[bestI]--;
            day++;
        }
        return ans;
    }
}
