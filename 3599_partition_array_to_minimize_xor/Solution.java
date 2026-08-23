// LeetCode 3599 - Partition Array to Minimize XOR
// https://leetcode.com/problems/partition-array-to-minimize-xor/

class Solution {
    public int minXor(int[] nums, int k) {
        int n = nums.length;
        int[] g = new int[n + 1];
        for (int i = 1; i <= n; i++) g[i] = g[i - 1] ^ nums[i - 1];
        final int Inf = Integer.MAX_VALUE / 2;
        int[][] f = new int[n + 1][];
        for (int i = 0; i <= n; i++) {
            f[i] = new int[k + 1];
            for (int j = 0; j <= k; j++) f[i][j] = Inf;
        }
        f[0][0] = 0;
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= Math.min(i, k); j++) {
                for (int h = j - 1; h < i; h++) {
                    f[i][j] = Math.min(f[i][j], Math.max(f[h][j - 1], g[i] ^ g[h]));
                }
            }
        }
        return f[n][k];
    }
}
