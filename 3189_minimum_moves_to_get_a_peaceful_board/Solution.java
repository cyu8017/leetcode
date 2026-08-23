// LeetCode 3189 - Minimum Moves to Get a Peaceful Board
// https://leetcode.com/problems/minimum-moves-to-get-a-peaceful-board/

import java.util.Arrays;

class Solution {
    public int minMoves(int[][] rooks) {
        int ans = 0;
        Arrays.sort(rooks, (a, b) -> Integer.compare(a[0], b[0]));
        for (int i = 0; i < rooks.length; i++) ans += Math.abs(rooks[i][0] - i);
        Arrays.sort(rooks, (a, b) -> Integer.compare(a[1], b[1]));
        for (int j = 0; j < rooks.length; j++) ans += Math.abs(rooks[j][1] - j);
        return ans;
    }
}
