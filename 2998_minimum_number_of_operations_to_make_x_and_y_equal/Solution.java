// LeetCode 2998 - Minimum Number of Operations to Make X and Y Equal
// https://leetcode.com/problems/minimum-number-of-operations-to-make-x-and-y-equal/

import java.util.ArrayDeque;
import java.util.HashSet;
import java.util.Queue;
import java.util.Set;

class Solution {
    public int minimumOperationsToMakeEqual(int x, int y) {
        if (x <= y) return y - x;
        Queue<int[]> q = new ArrayDeque<>();
        q.offer(new int[]{x, 0});
        Set<Integer> seen = new HashSet<>();
        seen.add(x);
        while (!q.isEmpty()) {
            int[] cur = q.poll();
            int v = cur[0], d = cur[1];
            if (v == y) return d;
            int[] cands = {v + 1, v - 1, v % 11 == 0 ? v / 11 : -1, v % 5 == 0 ? v / 5 : -1};
            for (int nxt : cands) {
                if (nxt > 0 && nxt < 2 * x + 20 && seen.add(nxt)) {
                    q.offer(new int[]{nxt, d + 1});
                }
            }
        }
        return -1;
    }
}
