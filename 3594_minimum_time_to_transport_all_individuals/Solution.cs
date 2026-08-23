// LeetCode 3594 - Minimum Time to Transport All Individuals
// https://leetcode.com/problems/minimum-time-to-transport-all-individuals/

using System;

public class Solution {
    public double MinTime(int n, int k, int m, int[] time, double[] mul) {
        int[] t = (int[])time.Clone();
        Array.Sort(t);
        double total = 0;
        int stage = 0, left = n;
        while (left > 0) {
            int take = Math.Min(k, left);
            int slow = t[left - 1];
            total += (double)slow * mul[stage % m];
            left -= take;
            stage++;
            if (left > 0) {
                total += (double)t[0] * mul[stage % m];
                stage++;
            }
        }
        return total;
    }
}
