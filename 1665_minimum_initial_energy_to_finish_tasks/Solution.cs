// LeetCode 1665 - Minimum Initial Energy to Finish Tasks
// https://leetcode.com/problems/minimum-initial-energy-to-finish-tasks/

using System;

public class Solution {
    public int MinimumEffort(int[][] tasks) {
        Array.Sort(tasks, (a, b) => (b[1] - b[0]).CompareTo(a[1] - a[0]));
        int energy = 0, spent = 0;
        foreach (var t in tasks) {
            energy = Math.Max(energy, spent + t[1]);
            spent += t[0];
        }
        return energy;
    }
}
