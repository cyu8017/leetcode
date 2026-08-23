// LeetCode 0945 - Minimum Increment to Make Array Unique
// https://leetcode.com/problems/minimum-increment-to-make-array-unique/

using System;

public class Solution {
    public int MinIncrementForUnique(int[] nums) {
        Array.Sort(nums);
        int ans = 0;
        for (int i = 1; i < nums.Length; i++) {
            if (nums[i] <= nums[i - 1]) {
                int need = nums[i - 1] + 1;
                ans += need - nums[i];
                nums[i] = need;
            }
        }
        return ans;
    }
}
