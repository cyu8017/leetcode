// LeetCode 2640 - Find the Score of All Prefixes of an Array
// https://leetcode.com/problems/find-the-score-of-all-prefixes-of-an-array/

class Solution {
    public long[] findPrefixScore(int[] nums) {
        long[] ans = new long[nums.length];
        int mx = 0;
        long sum = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] > mx) mx = nums[i];
            sum += nums[i] + mx;
            ans[i] = sum;
        }
        return ans;
    }
}
