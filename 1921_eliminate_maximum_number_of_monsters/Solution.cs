// LeetCode 1921 - Eliminate Maximum Number of Monsters
// https://leetcode.com/problems/eliminate-maximum-number-of-monsters/

using System;

public class Solution {
    public int EliminateMaximum(int[] dist, int[] speed) {
        int n = dist.Length;
        var arrival = new int[n];
        for (int i = 0; i < n; i++)
            arrival[i] = (dist[i] + speed[i] - 1) / speed[i];
        Array.Sort(arrival);
        for (int i = 0; i < n; i++)
            if (arrival[i] <= i) return i;
        return n;
    }
}