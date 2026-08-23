// LeetCode 0473 - Matchsticks to Square
// https://leetcode.com/problems/matchsticks-to-square/

public class Solution {
    public bool Makesquare(int[] matchsticks) {
        if (matchsticks.Length == 0) {
            return false;
        }
        int total = matchsticks.Sum();
        if (total % 4 != 0) {
            return false;
        }
        int side = total / 4;
        int[] sticks = matchsticks.OrderByDescending(x => x).ToArray();
        return Dfs(0, sticks, new int[4], side);
    }

    private static bool Dfs(int index, int[] matchsticks, int[] sides, int side) {
        if (index == matchsticks.Length) {
            return sides.All(value => value == side);
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
            if (Dfs(index + 1, matchsticks, sides, side)) {
                return true;
            }
            sides[sideIndex] -= length;
        }
        return false;
    }
}
