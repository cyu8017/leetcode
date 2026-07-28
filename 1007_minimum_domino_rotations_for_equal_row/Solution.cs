// LeetCode 1007 - Minimum Domino Rotations For Equal Row
// https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/

public class Solution {
    public int MinDominoRotations(int[] tops, int[] bottoms) {
        int ans = Math.Min(Check(tops, bottoms, tops[0]), Check(tops, bottoms, bottoms[0]));
        return ans == int.MaxValue ? -1 : ans;
    }

    private static int Check(int[] tops, int[] bottoms, int target) {
        int rotTop = 0, rotBot = 0;
        for (int i = 0; i < tops.Length; i++) {
            if (tops[i] != target && bottoms[i] != target) return int.MaxValue;
            if (tops[i] != target) rotTop++;
            if (bottoms[i] != target) rotBot++;
        }
        return Math.Min(rotTop, rotBot);
    }
}
