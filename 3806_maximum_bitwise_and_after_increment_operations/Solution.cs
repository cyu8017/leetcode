// LeetCode 3806 - Maximum Bitwise And After Increment Operations
// https://leetcode.com/problems/maximum-bitwise-and-after-increment-operations/

using System;

public class Solution {
    static int BitLen(uint x) {
        if (x == 0) return 0;
        int n = 0;
        while (x > 0) { n++; x >>= 1; }
        return n;
    }

    public int MaximumAND(int[] nums, int k, int m) {
        int mxVal = nums[0];
        foreach (int v in nums) if (v > mxVal) mxVal = v;
        mxVal += k;
        int mx = BitLen((uint)mxVal);
        int ans = 0;
        int[] cost = new int[nums.Length];
        for (int bit = mx - 1; bit >= 0; bit--) {
            int target = ans | (1 << bit);
            for (int i = 0; i < nums.Length; i++) {
                int x = nums[i];
                int j = BitLen((uint)(target & ~x));
                int mask = (1 << j) - 1;
                cost[i] = (target & mask) - (x & mask);
            }
            Array.Sort(cost);
            int sum = 0;
            for (int i = 0; i < m; i++) sum += cost[i];
            if (sum <= k) ans = target;
        }
        return ans;
    }
}
