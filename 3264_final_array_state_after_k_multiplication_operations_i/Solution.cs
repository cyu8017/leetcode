// LeetCode 3264 - Final Array State After K Multiplication Operations I
// https://leetcode.com/problems/final-array-state-after-k-multiplication-operations-i/

using System;
using System.Collections.Generic;

public class Solution {
    public int[] GetFinalState(int[] nums, int k, int multiplier) {
        var h = new PriorityQueue<int, (int, int)>();
        for (int i = 0; i < nums.Length; i++) h.Enqueue(i, (nums[i], i));
        for (int t = 0; t < k; t++) {
            int i = h.Dequeue();
            nums[i] *= multiplier;
            h.Enqueue(i, (nums[i], i));
        }
        return nums;
    }
}
