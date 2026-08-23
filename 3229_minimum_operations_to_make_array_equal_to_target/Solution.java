// LeetCode 3229 - Minimum Operations to Make Array Equal to Target
// https://leetcode.com/problems/minimum-operations-to-make-array-equal-to-target/

class Solution {
    public long minimumOperations(int[] nums, int[] target) {
        long f = Math.abs(target[0] - nums[0]);
        for (int i = 1; i < target.length; i++) {
            int x = target[i] - nums[i];
            int y = target[i - 1] - nums[i - 1];
            if ((long) x * y > 0) {
                int d = Math.abs(x) - Math.abs(y);
                if (d > 0) {
                    f += d;
                }
            } else {
                f += Math.abs(x);
            }
        }
        return f;
    }
}
