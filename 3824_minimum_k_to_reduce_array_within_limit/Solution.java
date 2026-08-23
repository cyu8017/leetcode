// LeetCode 3824 - Minimum K To Reduce Array Within Limit
// https://leetcode.com/problems/minimum_k_to_reduce_array_within_limit/

class Solution {
    public int minimumK(int[] nums) {
        int lo = 1, hi = 100000;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (check(nums, mid)) hi = mid;
            else lo = mid + 1;
        }
        return lo;
    }

    private boolean check(int[] nums, int k) {
        long t = 0;
        for (int x : nums) t += (x + k - 1) / k;
        return t <= 1L * k * k;
    }
}
