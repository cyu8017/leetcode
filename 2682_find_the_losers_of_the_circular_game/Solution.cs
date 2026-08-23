// LeetCode 2682 - Find the Losers of the Circular Game
// https://leetcode.com/problems/find-the-losers-of-the-circular-game/

using System.Collections.Generic;

public class Solution {
    public int[] CircularGameLosers(int n, int k) {
        bool[] seen = new bool[n + 1];
        int cur = 1, step = 1;
        while (!seen[cur]) {
            seen[cur] = true;
            cur = (cur - 1 + step * k) % n + 1;
            step++;
        }
        var ans = new List<int>();
        for (int i = 1; i <= n; i++) if (!seen[i]) ans.Add(i);
        return ans.ToArray();
    }
}
