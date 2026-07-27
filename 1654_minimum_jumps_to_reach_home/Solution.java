// LeetCode 1654 - Minimum Jumps to Reach Home
// https://leetcode.com/problems/minimum-jumps-to-reach-home/

import java.util.ArrayDeque;
import java.util.HashSet;
import java.util.Queue;
import java.util.Set;

class Solution {
    public int minimumJumps(int[] forbidden, int a, int b, int x) {
        Set<Integer> bad = new HashSet<>();
        int maxForbidden = 0;
        for (int f : forbidden) {
            bad.add(f);
            maxForbidden = Math.max(maxForbidden, f);
        }
        int limit = Math.max(x, maxForbidden) + a + b;
        Queue<int[]> queue = new ArrayDeque<>();
        queue.offer(new int[] {0, 0, 0});
        Set<Long> seen = new HashSet<>();
        seen.add(0L);
        while (!queue.isEmpty()) {
            int[] cur = queue.poll();
            int pos = cur[0];
            int dist = cur[1];
            boolean back = cur[2] == 1;
            if (pos == x) {
                return dist;
            }
            int[][] next = {{pos + a, 0}, {pos - b, 1}};
            for (int[] step : next) {
                int np = step[0];
                boolean nb = step[1] == 1;
                if (np < 0 || np > limit || bad.contains(np)) {
                    continue;
                }
                if (back && nb) {
                    continue;
                }
                long key = (((long) np) << 1) | (nb ? 1 : 0);
                if (seen.add(key)) {
                    queue.offer(new int[] {np, dist + 1, nb ? 1 : 0});
                }
            }
        }
        return -1;
    }
}
