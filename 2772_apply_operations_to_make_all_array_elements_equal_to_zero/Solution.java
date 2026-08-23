// LeetCode 2772 - Apply Operations to Make All Array Elements Equal to Zero
// https://leetcode.com/problems/apply-operations-to-make-all-array-elements-equal-to-zero/

class Solution {
    public boolean checkArray(int[] nums, int k) {
        int n = nums.length;
        int[] diff = new int[n + 1];
        int cur = 0;
        for (int i = 0; i < n; i++) {
            cur += diff[i];
            int need = nums[i] - cur;
            if (need < 0) return false;
            if (need > 0) {
                if (i + k > n) return false;
                cur += need;
                diff[i + k] -= need;
            }
        }
        return true;
    }
}
