// LeetCode 0913 - Cat and Mouse
// https://leetcode.com/problems/cat-and-mouse/

using System.Collections.Generic;

public class Solution {
    public int CatMouseGame(int[][] graph) {
        int n = graph.Length;
        const int DRAW = 0, MOUSE_WIN = 1, CAT_WIN = 2;
        int[,,] states = new int[n, n, 2];
        int[,,] outDegree = new int[n, n, 2];
        var q = new Queue<(int cat, int mouse, int move, int state)>();

        for (int cat = 0; cat < n; cat++) {
            for (int mouse = 0; mouse < n; mouse++) {
                outDegree[cat, mouse, 0] = graph[mouse].Length;
                int deg = 0;
                foreach (int x in graph[cat]) if (x != 0) deg++;
                outDegree[cat, mouse, 1] = deg;
            }
        }
        for (int cat = 1; cat < n; cat++) {
            for (int move = 0; move < 2; move++) {
                states[cat, 0, move] = MOUSE_WIN;
                q.Enqueue((cat, 0, move, MOUSE_WIN));
                states[cat, cat, move] = CAT_WIN;
                q.Enqueue((cat, cat, move, CAT_WIN));
            }
        }
        while (q.Count > 0) {
            var (cat, mouse, move, state) = q.Dequeue();
            if (cat == 2 && mouse == 1 && move == 0) return state;
            int prevMove = move ^ 1;
            foreach (int prev in graph[prevMove == 1 ? cat : mouse]) {
                int prevCat = prevMove == 1 ? prev : cat;
                if (prevCat == 0) continue;
                int prevMouse = prevMove == 1 ? mouse : prev;
                if (states[prevCat, prevMouse, prevMove] != 0) continue;
                if ((prevMove == 0 && state == MOUSE_WIN) ||
                    (prevMove == 1 && state == CAT_WIN) ||
                    outDegree[prevCat, prevMouse, prevMove] == 1) {
                    states[prevCat, prevMouse, prevMove] = state;
                    q.Enqueue((prevCat, prevMouse, prevMove, state));
                } else {
                    outDegree[prevCat, prevMouse, prevMove]--;
                }
            }
        }
        return states[2, 1, 0];
    }
}
