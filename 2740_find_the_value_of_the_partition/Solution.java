// LeetCode 2740 - Find the Value of the Partition
// https://leetcode.com/problems/find-the-value-of-the-partition/

import java.util.Arrays;

class Solution {
    public int findValueOfPartition(int[] nums) {
        Arrays.sort(nums);
        int ans = Integer.MAX_VALUE;
        for (int i = 1; i < nums.length; i++)
            ans = Math.min(ans, nums[i] - nums[i - 1]);
        return ans;
    }
}
