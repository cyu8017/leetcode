// LeetCode 0473 - Matchsticks to Square
// https://leetcode.com/problems/matchsticks-to-square/

import java.util.Arrays;

class Solution {
    public boolean makesquare(int[] matchsticks) {
        if (matchsticks.length == 0) {
            return false;
        }
        int total = 0;
        for (int length : matchsticks) {
            total += length;
        }
        if (total % 4 != 0) {
            return false;
        }
        int side = total / 4;
        Integer[] sorted = new Integer[matchsticks.length];
        for (int i = 0; i < matchsticks.length; i++) {
            sorted[i] = matchsticks[i];
        }
        Arrays.sort(sorted, (a, b) -> b - a);
        int[] sticks = new int[sorted.length];
        for (int i = 0; i < sorted.length; i++) {
            sticks[i] = sorted[i];
        }
        return dfs(0, sticks, new int[4], side);
    }

    private boolean dfs(int index, int[] matchsticks, int[] sides, int side) {
        if (index == matchsticks.length) {
            return sides[0] == side && sides[1] == side && sides[2] == side && sides[3] == side;
        }
        int length = matchsticks[index];
        for (int sideIndex = 0; sideIndex < 4; sideIndex++) {
            if (sides[sideIndex] + length > side) {
                continue;
            }
            if (sideIndex > 0 && sides[sideIndex] == sides[sideIndex - 1]) {
                continue;
            }
            sides[sideIndex] += length;
            if (dfs(index + 1, matchsticks, sides, side)) {
                return true;
            }
            sides[sideIndex] -= length;
        }
        return false;
    }
}
