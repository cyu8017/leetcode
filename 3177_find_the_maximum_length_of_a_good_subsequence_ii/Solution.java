// LeetCode 3177 - Find the Maximum Length of a Good Subsequence II
// https://leetcode.com/problems/find-the-maximum-length-of-a-good-subsequence-ii/

import java.util.HashMap;
import java.util.Map;

class Solution {
    public int maximumLength(int[] nums, int k) {
        int n = nums.length;
        int[][] f = new int[n][k + 1];
        @SuppressWarnings("unchecked")
        Map<Integer, Integer>[] mp = new HashMap[k + 1];
        for (int h = 0; h <= k; h++) {
            mp[h] = new HashMap<>();
        }
        int[][] g = new int[k + 1][3];
        int ans = 0;
        for (int i = 0; i < n; i++) {
            for (int h = 0; h <= k; h++) {
                f[i][h] = mp[h].getOrDefault(nums[i], 0);
                if (h > 0) {
                    if (g[h - 1][0] != nums[i]) {
                        f[i][h] = Math.max(f[i][h], g[h - 1][1]);
                    } else {
                        f[i][h] = Math.max(f[i][h], g[h - 1][2]);
                    }
                }
                f[i][h]++;
                mp[h].put(nums[i], Math.max(mp[h].getOrDefault(nums[i], 0), f[i][h]));
                if (g[h][0] != nums[i]) {
                    if (f[i][h] >= g[h][1]) {
                        g[h][2] = g[h][1];
                        g[h][1] = f[i][h];
                        g[h][0] = nums[i];
                    } else if (f[i][h] > g[h][2]) {
                        g[h][2] = f[i][h];
                    }
                } else if (f[i][h] > g[h][1]) {
                    g[h][1] = f[i][h];
                }
                ans = Math.max(ans, f[i][h]);
            }
        }
        return ans;
    }
}
