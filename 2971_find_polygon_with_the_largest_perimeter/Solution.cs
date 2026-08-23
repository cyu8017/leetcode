// LeetCode 2971 - Find Polygon With the Largest Perimeter
// https://leetcode.com/problems/find-polygon-with-the-largest-perimeter/

using System;

public class Solution {
    public long LargestPerimeter(int[] nums) {
        Array.Sort(nums);
        long sum = 0;
        foreach (int v in nums) sum += v;
        for (int i = nums.Length - 1; i >= 2; i--) {
            sum -= nums[i];
            if (sum > nums[i]) return sum + nums[i];
        }
        return -1;
    }
}
