// LeetCode 0798 - Smallest Rotation with Highest Score
// https://leetcode.com/problems/smallest-rotation-with-highest-score/

using System;

public class Solution {
    public int BestRotation(int[] nums) {
        int n = nums.Length;
        int[] change = new int[n];
        Array.Fill(change, 1);
        for (int i = 0; i < n; i++) change[(i - nums[i] + 1 + n) % n] -= 1;
        for (int i = 1; i < n; i++) change[i] += change[i - 1];
        int best = 0;
        for (int i = 1; i < n; i++) if (change[i] > change[best]) best = i;
        return best;
    }
}
