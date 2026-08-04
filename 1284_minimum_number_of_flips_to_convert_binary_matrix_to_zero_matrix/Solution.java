// LeetCode 1284 - Minimum Number of Flips to Convert Binary Matrix to Zero Matrix
// https://leetcode.com/problems/minimum-number-of-flips-to-convert-binary-matrix-to-zero-matrix/

import java.util.*;

class Solution {
    public int minFlips(int[][] mat) {
        int m = mat.length, n = mat[0].length;
        int start = 0;
        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                if (mat[r][c] != 0) start |= 1 << (r * n + c);
            }
        }
        int[][] deltas = {{0, 0}, {1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        List<Integer> masks = new ArrayList<>();
        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                int mask = 0;
                for (int[] d : deltas) {
                    int nr = r + d[0], nc = c + d[1];
                    if (nr >= 0 && nr < m && nc >= 0 && nc < n) mask ^= 1 << (nr * n + nc);
                }
                masks.add(mask);
            }
        }
        ArrayDeque<int[]> queue = new ArrayDeque<>();
        HashSet<Integer> seen = new HashSet<>();
        queue.add(new int[] {start, 0});
        seen.add(start);
        while (!queue.isEmpty()) {
            int[] cur = queue.poll();
            if (cur[0] == 0) return cur[1];
            for (int mask : masks) {
                int nxt = cur[0] ^ mask;
                if (seen.add(nxt)) queue.add(new int[] {nxt, cur[1] + 1});
            }
        }
        return -1;
    }
}
