// LeetCode 3355 - Zero Array Transformation I
// https://leetcode.com/problems/zero-array-transformation-i/

class Solution {
    public boolean isZeroArray(int[] nums, int[][] queries) {
        int n = nums.length;
        int[] diff = new int[n + 1];
        for (var q : queries) {
            diff[q[0]]++;
            diff[q[1] + 1]--;
        }
        int cur = 0;
        for (int i = 0; i < n; i++) {
            cur += diff[i];
            if (cur < nums[i]) return false;
        }
        return true;
    }
}
