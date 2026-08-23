// LeetCode 3833 - Count Dominant Indices
// https://leetcode.com/problems/count-dominant-indices/

class Solution {
    public int dominantIndices(int[] nums) {
        int n = nums.length, ans = 0, suf = nums[n - 1];
        for (int i = n - 2; i >= 0; i--) {
            if (nums[i] * (n - i - 1) > suf) ans++;
            suf += nums[i];
        }
        return ans;
    }
}
