// LeetCode 3247 - Number of Subsequences with Odd Sum
// https://leetcode.com/problems/number-of-subsequences-with-odd-sum/

class Solution {
    public int subsequenceCount(int[] nums) {
        final int mod = 1000000007;
        int[] f = new int[2];
        for (int x : nums) {
            int[] g = new int[2];
            if (x % 2 == 1) {
                g[0] = (f[0] + f[1]) % mod;
                g[1] = (f[0] + f[1] + 1) % mod;
            } else {
                g[0] = (f[0] + f[0] + 1) % mod;
                g[1] = (f[1] + f[1]) % mod;
            }
            f = g;
        }
        return f[1];
    }
}
