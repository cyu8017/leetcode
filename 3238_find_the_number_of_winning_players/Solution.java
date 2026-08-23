// LeetCode 3238 - Find the Number of Winning Players
// https://leetcode.com/problems/find-the-number-of-winning-players/

import java.util.HashSet;
import java.util.Set;

class Solution {
    public int winningPlayerCount(int n, int[][] pick) {
        int[][] cnt = new int[n][];
        for (int i = 0; i < n; i++) cnt[i] = new int[11];
        var s = new HashSet<Integer>();
        for (var p : pick) {
            int x = p[0], y = p[1];
            cnt[x][y]++;
            if (cnt[x][y] > x) s.add(x);
        }
        return s.size();
    }
}
