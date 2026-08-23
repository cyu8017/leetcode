// LeetCode 2560 - House Robber IV
// https://leetcode.com/problems/house-robber-iv/

class Solution {
    public int minCapability(int[] nums, int k) {
        int lo = Integer.MAX_VALUE, hi = Integer.MIN_VALUE;
        for (int x : nums) {
            if (x < lo) lo = x;
            if (x > hi) hi = x;
        }
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (ok(nums, k, mid)) hi = mid;
            else lo = mid + 1;
        }
        return lo;
    }

    private boolean ok(int[] nums, int k, int cap) {
        int cnt = 0;
        for (int i = 0; i < nums.length;) {
            if (nums[i] <= cap) {
                cnt++;
                i += 2;
            } else i++;
        }
        return cnt >= k;
    }
}
