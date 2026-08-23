// LeetCode 0611 - Valid Triangle Number
// https://leetcode.com/problems/valid-triangle-number/

using System;

public class Solution {
    public int TriangleNumber(int[] nums) {
        Array.Sort(nums);
        int n = nums.Length, count = 0;
        for (int k = n - 1; k >= 2; --k) {
            int left = 0, right = k - 1;
            while (left < right) {
                if (nums[left] + nums[right] > nums[k]) {
                    count += right - left;
                    --right;
                } else {
                    ++left;
                }
            }
        }
        return count;
    }
}
