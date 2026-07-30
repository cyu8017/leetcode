// LeetCode 1503 - Last Moment Before All Ants Fall Out of a Plank
// https://leetcode.com/problems/last-moment-before-all-ants-fall-out-of-a-plank/

using System;
using System.Linq;

public class Solution {
    public int GetLastMoment(int n, int[] left, int[] right) {
        int leftMax = left.Length == 0 ? 0 : left.Max();
        int rightMin = right.Length == 0 ? n : right.Min();
        return Math.Max(leftMax, n - rightMin);
    }
}
