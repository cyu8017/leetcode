// LeetCode 2056 - Number of Valid Move Combinations On Chessboard
// https://leetcode.com/problems/number-of-valid-move-combinations-on-chessboard/

import java.util.*;

class Solution {
    private static class Move {
        int dr, dc, steps;
        Move(int dr, int dc, int steps) { this.dr = dr; this.dc = dc; this.steps = steps; }
    }

    private String[] pieces;
    private int[][] positions;
    private List<Move>[] allMoves;
    private Move[] chosen;
    private int ans;

    public int countCombinations(String[] pieces, int[][] positions) {
        this.pieces = pieces;
        this.positions = positions;
        Map<String, int[][]> dirs = new HashMap<>();
        dirs.put("rook", new int[][] {{1,0},{-1,0},{0,1},{0,-1}});
        dirs.put("bishop", new int[][] {{1,1},{1,-1},{-1,1},{-1,-1}});
        dirs.put("queen", new int[][] {{1,0},{-1,0},{0,1},{0,-1},{1,1},{1,-1},{-1,1},{-1,-1}});
        int n = pieces.length;
        allMoves = new ArrayList[n];
        for (int i = 0; i < n; i++) {
            List<Move> ms = new ArrayList<>();
            ms.add(new Move(0, 0, 0));
            int r = positions[i][0], c = positions[i][1];
            for (int[] d : dirs.get(pieces[i])) {
                int nr = r + d[0], nc = c + d[1], step = 1;
                while (nr >= 1 && nr <= 8 && nc >= 1 && nc <= 8) {
                    ms.add(new Move(d[0], d[1], step));
                    nr += d[0]; nc += d[1]; step++;
                }
            }
            allMoves[i] = ms;
        }
        chosen = new Move[n];
        ans = 0;
        dfs(0);
        return ans;
    }

    private boolean okCombo(int end) {
        int maxT = 0;
        for (int i = 0; i <= end; i++) maxT = Math.max(maxT, chosen[i].steps);
        for (int t = 1; t <= maxT; t++) {
            Set<Long> seen = new HashSet<>();
            for (int i = 0; i <= end; i++) {
                Move m = chosen[i];
                int pr, pc;
                if (m.steps == 0) { pr = positions[i][0]; pc = positions[i][1]; }
                else {
                    int use = Math.min(t, m.steps);
                    pr = positions[i][0] + m.dr * use;
                    pc = positions[i][1] + m.dc * use;
                }
                long key = (((long) pr) << 32) ^ (pc & 0xffffffffL);
                if (!seen.add(key)) return false;
            }
        }
        return true;
    }

    private void dfs(int i) {
        if (i == pieces.length) { ans++; return; }
        for (Move m : allMoves[i]) {
            chosen[i] = m;
            if (okCombo(i)) dfs(i + 1);
        }
    }
}
