// LeetCode 2386 - Find the K-Sum of an Array
// https://leetcode.com/problems/find-the-k-sum-of-an-array/

using System;
using System.Collections.Generic;

public class Solution {
    public long KSum(int[] nums, int k) {
        long total = 0;
        int[] absNums = new int[nums.Length];
        for (int i = 0; i < nums.Length; i++) {
            if (nums[i] >= 0) { total += nums[i]; absNums[i] = nums[i]; }
            else absNums[i] = -nums[i];
        }
        Array.Sort(absNums);
        var h = new PriorityQueue<(long sum, int i), long>();
        h.Enqueue((total, 0), -total);
        for (int t = 0; t < k - 1; t++) {
            var (sum, i) = h.Dequeue();
            if (i >= absNums.Length) continue;
            long s1 = sum - absNums[i];
            h.Enqueue((s1, i + 1), -s1);
            if (i > 0) {
                long s2 = sum - absNums[i] + absNums[i - 1];
                h.Enqueue((s2, i + 1), -s2);
            }
        }
        return h.Peek().sum;
    }
}
