// LeetCode 1810 - Minimum Path Cost in a Hidden Grid
// https://leetcode.com/problems/minimum-path-cost-in-a-hidden-grid/

import java.util.HashMap;
import java.util.Map;
import java.util.PriorityQueue;

interface GridMaster {
    boolean canMove(char direction);

    int move(char direction);

    boolean isTarget();
}

class Solution {
    private static final int[][] DELTAS = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
    private static final char[] DIRS = {'U', 'D', 'L', 'R'};
    private static final char[] OPP = {'D', 'U', 'R', 'L'};

    public int findShortestPath(GridMaster master) {
        Map<Long, Integer> moveCost = new HashMap<>();
        moveCost.put(key(0, 0), 0);
        int[] target = new int[2];
        boolean[] hasTarget = {false};

        if (master.isTarget()) {
            return 0;
        }

        dfs(master, 0, 0, moveCost, target, hasTarget);

        if (!hasTarget[0]) {
            return -1;
        }

        Map<Long, Integer> best = new HashMap<>();
        best.put(key(0, 0), 0);
        PriorityQueue<int[]> heap = new PriorityQueue<>((a, b) -> a[0] - b[0]);
        heap.offer(new int[] {0, 0, 0});

        while (!heap.isEmpty()) {
            int[] item = heap.poll();
            int dist = item[0];
            int r = item[1];
            int c = item[2];
            if (r == target[0] && c == target[1]) {
                return dist;
            }
            long currentKey = key(r, c);
            if (dist > best.getOrDefault(currentKey, Integer.MAX_VALUE)) {
                continue;
            }
            for (int[] delta : DELTAS) {
                int nr = r + delta[0];
                int nc = c + delta[1];
                long nextKey = key(nr, nc);
                if (!moveCost.containsKey(nextKey)) {
                    continue;
                }
                int nd = dist + moveCost.get(nextKey);
                if (nd < best.getOrDefault(nextKey, Integer.MAX_VALUE)) {
                    best.put(nextKey, nd);
                    heap.offer(new int[] {nd, nr, nc});
                }
            }
        }
        return -1;
    }

    private void dfs(
            GridMaster master,
            int r,
            int c,
            Map<Long, Integer> moveCost,
            int[] target,
            boolean[] hasTarget) {
        for (int i = 0; i < DIRS.length; i++) {
            char direction = DIRS[i];
            if (!master.canMove(direction)) {
                continue;
            }
            int cost = master.move(direction);
            int nr = r + DELTAS[i][0];
            int nc = c + DELTAS[i][1];
            long nextKey = key(nr, nc);
            if (!moveCost.containsKey(nextKey)) {
                moveCost.put(nextKey, cost);
                if (master.isTarget()) {
                    hasTarget[0] = true;
                    target[0] = nr;
                    target[1] = nc;
                }
                dfs(master, nr, nc, moveCost, target, hasTarget);
            }
            master.move(OPP[i]);
        }
    }

    private long key(int r, int c) {
        return ((long) r << 32) | (c & 0xffffffffL);
    }
}
