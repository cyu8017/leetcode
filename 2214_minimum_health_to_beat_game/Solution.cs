// LeetCode 2214 - Minimum Health to Beat Game
// https://leetcode.com/problems/minimum-health-to-beat-game/

using System;

public class Solution {
    public long MinimumHealth(int[] damage, int armor) {
        long sum = 0;
        int mx = 0;
        foreach (int d in damage) { sum += d; mx = Math.Max(mx, d); }
        return sum - Math.Min(armor, mx) + 1;
    }
}
