// LeetCode 1799 - Maximize Score After N Operations
// https://leetcode.com/problems/maximize-score-after-n-operations/

import java.util.Arrays;

class Solution {
    private int[] nums;
    private int[] memo;
    private int n;

    public int maxScore(int[] nums) {
        this.nums = nums;
        this.n = nums.length;
        this.memo = new int[1 << n];
        Arrays.fill(memo, -1);
        return dp(0);
    }

    private int dp(int mask) {
        if (mask == (1 << n) - 1) return 0;
        if (memo[mask] != -1) return memo[mask];
        int step = Integer.bitCount(mask) / 2 + 1;
        int best = 0;
        for (int i = 0; i < n; i++) {
            if ((mask >> i & 1) == 1) continue;
            for (int j = i + 1; j < n; j++) {
                if ((mask >> j & 1) == 1) continue;
                best = Math.max(
                    best,
                    step * gcd(nums[i], nums[j]) + dp(mask | (1 << i) | (1 << j))
                );
            }
        }
        memo[mask] = best;
        return best;
    }

    private int gcd(int a, int b) {
        while (b != 0) {
            int t = a % b;
            a = b;
            b = t;
        }
        return a;
    }
}
