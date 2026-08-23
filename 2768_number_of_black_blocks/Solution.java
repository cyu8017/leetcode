// LeetCode 2768 - Number of Black Blocks
// https://leetcode.com/problems/number-of-black-blocks/

import java.util.HashMap;
import java.util.Map;

class Solution {
    public long[] countBlackBlocks(int m, int n, int[][] coordinates) {
        Map<Long, Integer> cnt = new HashMap<>();
        for (int[] c : coordinates) {
            int x = c[0], y = c[1];
            for (int i = x - 1; i <= x; i++) {
                for (int j = y - 1; j <= y; j++) {
                    if (i >= 0 && j >= 0 && i < m - 1 && j < n - 1) {
                        long key = ((long) i << 32) | (j & 0xffffffffL);
                        cnt.put(key, cnt.getOrDefault(key, 0) + 1);
                    }
                }
            }
        }
        long[] ans = new long[5];
        ans[0] = 1L * (m - 1) * (n - 1);
        for (int v : cnt.values()) {
            ans[v]++;
            ans[0]--;
        }
        return ans;
    }
}
