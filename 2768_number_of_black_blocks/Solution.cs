// LeetCode 2768 - Number of Black Blocks
// https://leetcode.com/problems/number-of-black-blocks/

using System.Collections.Generic;

public class Solution {
    public long[] CountBlackBlocks(int m, int n, int[][] coordinates) {
        var cnt = new Dictionary<(int, int), int>();
        foreach (var c in coordinates) {
            int x = c[0], y = c[1];
            for (int i = x - 1; i <= x; i++) {
                for (int j = y - 1; j <= y; j++) {
                    if (i >= 0 && j >= 0 && i < m - 1 && j < n - 1) {
                        var key = (i, j);
                        if (!cnt.ContainsKey(key)) cnt[key] = 0;
                        cnt[key]++;
                    }
                }
            }
        }
        long[] ans = new long[5];
        ans[0] = 1L * (m - 1) * (n - 1);
        foreach (var v in cnt.Values) {
            ans[v]++;
            ans[0]--;
        }
        return ans;
    }
}
