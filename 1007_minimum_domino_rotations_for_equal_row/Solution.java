// LeetCode 1007 - Minimum Domino Rotations For Equal Row
// https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/

class Solution {
    public int minDominoRotations(int[] tops, int[] bottoms) {
        int ans = Math.min(check(tops, bottoms, tops[0]), check(tops, bottoms, bottoms[0]));
        return ans == Integer.MAX_VALUE / 2 ? -1 : ans;
    }

    private int check(int[] tops, int[] bottoms, int target) {
        int rotTop = 0, rotBot = 0;
        for (int i = 0; i < tops.length; i++) {
            if (tops[i] != target && bottoms[i] != target) return Integer.MAX_VALUE / 2;
            if (tops[i] != target) rotTop++;
            if (bottoms[i] != target) rotBot++;
        }
        return Math.min(rotTop, rotBot);
    }
}
