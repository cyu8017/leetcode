// LeetCode 2943 - Maximize Area of Square Hole in Grid
// https://leetcode.com/problems/maximize-area-of-square-hole-in-grid/

import java.util.Arrays;

class Solution {
    private int maxGap(int[] bars) {
        if (bars.length == 0) return 1;
        Arrays.sort(bars);
        int best = 1, cur = 1;
        for (int i = 1; i < bars.length; i++) {
            if (bars[i] == bars[i - 1] + 1) cur++;
            else cur = 1;
            if (cur > best) best = cur;
        }
        return best + 1;
    }

    public int maximizeSquareHoleArea(int n, int m, int[] hBars, int[] vBars) {
        int side = maxGap(hBars.clone());
        int vs = maxGap(vBars.clone());
        if (vs < side) side = vs;
        return side * side;
    }
}
