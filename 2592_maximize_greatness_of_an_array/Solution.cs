// LeetCode 2592 - Maximize Greatness of an Array
// https://leetcode.com/problems/maximize-greatness-of-an-array/

using System;

public class Solution {
    public int MaximizeGreatness(int[] nums) {
        Array.Sort(nums);
        int i = 0;
        foreach (int x in nums) {
            if (x > nums[i]) i++;
        }
        return i;
    }
}
