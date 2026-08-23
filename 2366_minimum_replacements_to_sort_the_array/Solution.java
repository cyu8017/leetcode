// LeetCode 2366 - Minimum Replacements to Sort the Array
// https://leetcode.com/problems/minimum-replacements-to-sort-the-array/

class Solution {
    public long minimumReplacement(int[] nums) {
        long ans = 0;
        int n = nums.length;
        int prev = nums[n - 1];
        for (int i = n - 2; i >= 0; i--) {
            if (nums[i] <= prev) { prev = nums[i]; continue; }
            int parts = (nums[i] + prev - 1) / prev;
            ans += parts - 1;
            prev = nums[i] / parts;
        }
        return ans;
    }
}
