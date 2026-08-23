// LeetCode 2682 - Find the Losers of the Circular Game
// https://leetcode.com/problems/find-the-losers-of-the-circular-game/

import java.util.*;

class Solution {
    public int[] circularGameLosers(int n, int k) {
        boolean[] seen = new boolean[n + 1];
        int cur = 1, step = 1;
        while (!seen[cur]) {
            seen[cur] = true;
            cur = (cur - 1 + step * k) % n + 1;
            step++;
        }
        List<Integer> ans = new ArrayList<>();
        for (int i = 1; i <= n; i++) if (!seen[i]) ans.add(i);
        int[] out = new int[ans.size()];
        for (int i = 0; i < ans.size(); i++) out[i] = ans.get(i);
        return out;
    }
}
