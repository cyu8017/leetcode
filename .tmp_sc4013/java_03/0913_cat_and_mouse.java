// LeetCode 0913 - Cat and Mouse
// https://leetcode.com/problems/cat-and-mouse/

import java.util.*;

class Solution {
    public int catMouseGame(int[][] graph) {
        int n = graph.length;
        final int DRAW = 0, MOUSE_WIN = 1, CAT_WIN = 2;
        int[][][] states = new int[n][n][2];
        int[][][] outDegree = new int[n][n][2];
        Queue<int[]> q = new ArrayDeque<>();

        for (int cat = 0; cat < n; cat++) {
            for (int mouse = 0; mouse < n; mouse++) {
                outDegree[cat][mouse][0] = graph[mouse].length;
                int deg = 0;
                for (int x : graph[cat]) if (x != 0) deg++;
                outDegree[cat][mouse][1] = deg;
            }
        }
        for (int cat = 1; cat < n; cat++) {
            for (int move = 0; move < 2; move++) {
                states[cat][0][move] = MOUSE_WIN;
                q.offer(new int[] {cat, 0, move, MOUSE_WIN});
                states[cat][cat][move] = CAT_WIN;
                q.offer(new int[] {cat, cat, move, CAT_WIN});
            }
        }
        while (!q.isEmpty()) {
            int[] cur = q.poll();
            int cat = cur[0], mouse = cur[1], move = cur[2], state = cur[3];
            if (cat == 2 && mouse == 1 && move == 0) return state;
            int prevMove = move ^ 1;
            for (int prev : graph[prevMove == 1 ? cat : mouse]) {
                int prevCat = prevMove == 1 ? prev : cat;
                if (prevCat == 0) continue;
                int prevMouse = prevMove == 1 ? mouse : prev;
                if (states[prevCat][prevMouse][prevMove] != 0) continue;
                if ((prevMove == 0 && state == MOUSE_WIN) ||
                    (prevMove == 1 && state == CAT_WIN) ||
                    outDegree[prevCat][prevMouse][prevMove] == 1) {
                    states[prevCat][prevMouse][prevMove] = state;
                    q.offer(new int[] {prevCat, prevMouse, prevMove, state});
                } else {
                    outDegree[prevCat][prevMouse][prevMove]--;
                }
            }
        }
        return states[2][1][0];
    }
}
