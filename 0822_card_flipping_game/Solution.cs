// LeetCode 0822 - Card Flipping Game
// https://leetcode.com/problems/card-flipping-game/

using System;
using System.Collections.Generic;

public class Solution {
    public int Flipgame(int[] fronts, int[] backs) {
        var same = new HashSet<int>();
        for (int i = 0; i < fronts.Length; i++)
            if (fronts[i] == backs[i]) same.Add(fronts[i]);
        int best = int.MaxValue;
        foreach (int x in fronts) if (!same.Contains(x)) best = Math.Min(best, x);
        foreach (int x in backs) if (!same.Contains(x)) best = Math.Min(best, x);
        return best == int.MaxValue ? 0 : best;
    }
}
