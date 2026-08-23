// LeetCode 2943 - Maximize Area of Square Hole in Grid
// https://leetcode.com/problems/maximize-area-of-square-hole-in-grid/

using System;

public class Solution {
    public int MaximizeSquareHoleArea(int n, int m, int[] hBars, int[] vBars) {
        int MaxGap(int[] bars) {
            if (bars.Length == 0) return 1;
            Array.Sort(bars);
            int best = 1, cur = 1;
            for (int i = 1; i < bars.Length; i++) {
                if (bars[i] == bars[i - 1] + 1) cur++;
                else cur = 1;
                if (cur > best) best = cur;
            }
            return best + 1;
        }
        int side = MaxGap((int[])hBars.Clone());
        int vs = MaxGap((int[])vBars.Clone());
        if (vs < side) side = vs;
        return side * side;
    }
}
