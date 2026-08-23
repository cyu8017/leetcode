// LeetCode 3806 - Maximum Bitwise And After Increment Operations
// https://leetcode.com/problems/maximum-bitwise-and-after-increment-operations/

import java.util.Arrays;

class Solution {
    static int BitLen(int x) {
        if (x == 0) return 0;
        int n = 0;
        while (x > 0) { n++; x >>= 1; }
        return n;
    }

    public int maximumAND(int[] nums, int k, int m) {
        int mxVal = nums[0];
        for (int v : nums) if (v > mxVal) mxVal = v;
        mxVal += k;
        int mx = BitLen((int)mxVal);
        int ans = 0;
        int[] cost = new int[nums.length];
        for (int bit = mx - 1; bit >= 0; bit--) {
            int target = ans | (1 << bit);
            for (int i = 0; i < nums.length; i++) {
                int x = nums[i];
                int j = BitLen((int)(target & ~x));
                int mask = (1 << j) - 1;
                cost[i] = (target & mask) - (x & mask);
            }
            Arrays.sort(cost);
            int sum = 0;
            for (int i = 0; i < m; i++) sum += cost[i];
            if (sum <= k) ans = target;
        }
        return ans;
    }
}
