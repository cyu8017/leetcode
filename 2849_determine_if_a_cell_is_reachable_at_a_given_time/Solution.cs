// LeetCode 2849 - Determine if a Cell Is Reachable at a Given Time
// https://leetcode.com/problems/determine-if-a-cell-is-reachable-at-a-given-time/

using System;

public class Solution {
    public bool IsReachableAtTime(int sx, int sy, int fx, int fy, int t) {
        int need = Math.Max(Math.Abs(sx - fx), Math.Abs(sy - fy));
        if (need == 0) return t != 1;
        return t >= need;
    }
}
