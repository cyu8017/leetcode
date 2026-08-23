// LeetCode 2833 - Furthest Point From Origin
// https://leetcode.com/problems/furthest-point-from-origin/

using System;

public class Solution {
    public int FurthestDistanceFromOrigin(string moves) {
        int L = 0, R = 0, u = 0;
        foreach (char c in moves) {
            if (c == 'L') L++;
            else if (c == 'R') R++;
            else u++;
        }
        return Math.Abs(L - R) + u;
    }
}
