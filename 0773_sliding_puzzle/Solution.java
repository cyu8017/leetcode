// LeetCode 0773 - Sliding Puzzle
// https://leetcode.com/problems/sliding-puzzle/

import java.util.*;

class Solution {
    public int slidingPuzzle(int[][] board) {
        StringBuilder start = new StringBuilder();
        for (int[] row : board) for (int cell : row) start.append(cell);
        final String target = "123450";
        int[][] neighbors = {{1, 3}, {0, 2, 4}, {1, 5}, {0, 4}, {1, 3, 5}, {2, 4}};
        Queue<String> q = new ArrayDeque<>();
        Queue<Integer> stepsQ = new ArrayDeque<>();
        Set<String> seen = new HashSet<>();
        seen.add(start.toString());
        q.offer(start.toString());
        stepsQ.offer(0);
        while (!q.isEmpty()) {
            String state = q.poll();
            int steps = stepsQ.poll();
            if (state.equals(target)) return steps;
            int zero = state.indexOf('0');
            for (int nei : neighbors[zero]) {
                char[] nxt = state.toCharArray();
                char tmp = nxt[zero];
                nxt[zero] = nxt[nei];
                nxt[nei] = tmp;
                String ns = new String(nxt);
                if (seen.add(ns)) {
                    q.offer(ns);
                    stepsQ.offer(steps + 1);
                }
            }
        }
        return -1;
    }
}
