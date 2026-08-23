// LeetCode 3422 - Minimum Operations to Make Subarray Elements Equal
// https://leetcode.com/problems/minimum-operations-to-make-subarray-elements-equal/

import java.util.Arrays;

class Solution {
    public long minOperations(int[] nums, int k) {
        int n = nums.length;
        long ans = 1L << 62;
        for (int i = 0; i + k <= n; i++) {
            int[] sub = Arrays.copyOfRange(nums, i, i + k);
            Arrays.sort(sub);
            int med = sub[k / 2];
            long cost = 0;
            for (int x : sub) cost += Math.abs(x - med);
            if (cost < ans) ans = cost;
        }
        return ans;
    }
}
