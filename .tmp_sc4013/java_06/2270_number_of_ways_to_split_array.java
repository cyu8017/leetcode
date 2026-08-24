// LeetCode 2270 - Number of Ways to Split Array
// https://leetcode.com/problems/number-of-ways-to-split-array/

class Solution {
    public int waysToSplitArray(int[] nums) {
        long total = 0;
        for (int v : nums) total += v;
        long left = 0;
        int ans = 0;
        for (int i = 0; i + 1 < nums.length; i++) {
            left += nums[i];
            if (left >= total - left) ans++;
        }
        return ans;
    }
}
