// LeetCode 0740 - Delete and Earn
// https://leetcode.com/problems/delete-and-earn/

using System;
using System.Linq;

public class Solution {
    public int DeleteAndEarn(int[] nums) {
        if (nums.Length == 0) return 0;
        int maxNum = nums.Max();
        int[] points = new int[maxNum + 1];
        foreach (int num in nums) points[num] += num;
        int take = 0, skip = 0;
        foreach (int value in points) {
            int newTake = skip + value;
            int newSkip = Math.Max(skip, take);
            take = newTake;
            skip = newSkip;
        }
        return Math.Max(take, skip);
    }
}
