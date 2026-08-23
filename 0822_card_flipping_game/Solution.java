// LeetCode 0822 - Card Flipping Game
// https://leetcode.com/problems/card-flipping-game/

import java.util.*;

class Solution {
    public int flipgame(int[] fronts, int[] backs) {
        Set<Integer> same = new HashSet<>();
        for (int i = 0; i < fronts.length; i++) {
            if (fronts[i] == backs[i]) same.add(fronts[i]);
        }
        int best = Integer.MAX_VALUE;
        for (int x : fronts) if (!same.contains(x)) best = Math.min(best, x);
        for (int x : backs) if (!same.contains(x)) best = Math.min(best, x);
        return best == Integer.MAX_VALUE ? 0 : best;
    }
}
