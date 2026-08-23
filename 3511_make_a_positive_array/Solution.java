// LeetCode 3511 - Make a Positive Array
// https://leetcode.com/problems/make-a-positive-array/

class Solution {
    public int makeArrayPositive(int[] nums) {
        int ans = 0, l = -1;
        long preMx = 0, s = 0;
        for (int r = 0; r < nums.length; r++) {
            s += nums[r];
            if (r - l > 2 && s <= preMx) {
                ans++;
                l = r;
                preMx = 0;
                s = 0;
            } else if (r - l >= 2) {
                preMx = Math.max(preMx, s - nums[r] - nums[r - 1]);
            }
        }
        return ans;
    }
}
