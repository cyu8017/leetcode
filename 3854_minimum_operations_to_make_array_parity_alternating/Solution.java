// LeetCode 3854 - Minimum Operations To Make Array Parity Alternating
// https://leetcode.com/problems/minimum-operations-to-make-array-parity-alternating/

class Solution {
    public int[] makeParityAlternating(int[] nums) {
        if (nums.length == 1) return new int[] { 0, 0 };
        int mn = nums[0], mx = nums[0];
        for (int x : nums) { mn = Math.min(mn, x); mx = Math.max(mx, x); }
        int[] r0 = f(nums, 0, mn, mx);
        int[] r1 = f(nums, 1, mn, mx);
        if (r0[0] != r1[0]) return r0[0] < r1[0] ? r0 : r1;
        return r0[1] <= r1[1] ? r0 : r1;
    }

    private int[] f(int[] nums, int k, int mn, int mx) {
        int cnt = 0, a = Integer.MAX_VALUE, b = Integer.MIN_VALUE;
        for (int i = 0; i < nums.length; i++) {
            int x = nums[i];
            if (((x - i) & 1) != k) {
                cnt++;
                if (x == mn) x++;
                else if (x == mx) x--;
            }
            a = Math.min(a, x);
            b = Math.max(b, x);
        }
        return new int[] { cnt, Math.max(1, b - a) };
    }
}
