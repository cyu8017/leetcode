// LeetCode 2897 - Apply Operations on Array to Maximize Sum of Squares
// https://leetcode.com/problems/apply-operations-on-array-to-maximize-sum-of-squares/

class Solution {
    public int maxSum(int[] nums, int k) {
        final int mod = 1000000007;
        int[] cnt = new int[32];
        for (int v : nums)
            for (int b = 0; b < 32; b++)
                if ((v & (1 << b)) != 0) cnt[b]++;
        int ans = 0;
        for (int i = 0; i < k; i++) {
            int cur = 0;
            for (int b = 0; b < 32; b++) {
                if (cnt[b] > 0) {
                    cur |= 1 << b;
                    cnt[b]--;
                }
            }
            ans = (int) ((ans + 1L * (cur % mod) * (cur % mod) % mod) % mod);
        }
        return ans;
    }
}
