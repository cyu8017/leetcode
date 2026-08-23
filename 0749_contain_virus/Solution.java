// LeetCode 0749 - Contain Virus
// https://leetcode.com/problems/contain-virus/

import java.util.*;

class Solution {
    public int containVirus(int[][] isInfected) {
        int m = isInfected.length, n = isInfected[0].length, walls = 0;
        while (true) {
            Set<Long> seen = new HashSet<>();
            List<Set<Long>> regions = new ArrayList<>();
            List<Set<Long>> frontiers = new ArrayList<>();
            List<Integer> perimeters = new ArrayList<>();
            for (int i = 0; i < m; i++) {
                for (int j = 0; j < n; j++) {
                    long key = (((long) i) << 32) | (j & 0xffffffffL);
                    if (isInfected[i][j] == 1 && !seen.contains(key)) {
                        List<long[]> stack = new ArrayList<>();
                        stack.add(new long[] {i, j});
                        seen.add(key);
                        Set<Long> region = new HashSet<>();
                        Set<Long> frontier = new HashSet<>();
                        int perimeter = 0;
                        int[][] dirs = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
                        while (!stack.isEmpty()) {
                            long[] cur = stack.remove(stack.size() - 1);
                            int r = (int) cur[0], c = (int) cur[1];
                            region.add((((long) r) << 32) | (c & 0xffffffffL));
                            for (int[] d : dirs) {
                                int nr = r + d[0], nc = c + d[1];
                                if (nr < 0 || nr >= m || nc < 0 || nc >= n) continue;
                                long nk = (((long) nr) << 32) | (nc & 0xffffffffL);
                                if (isInfected[nr][nc] == 1 && seen.add(nk)) stack.add(new long[] {nr, nc});
                                else if (isInfected[nr][nc] == 0) { frontier.add(nk); perimeter++; }
                            }
                        }
                        regions.add(region);
                        frontiers.add(frontier);
                        perimeters.add(perimeter);
                    }
                }
            }
            if (regions.isEmpty()) break;
            int quarantine = 0;
            for (int i = 1; i < regions.size(); i++)
                if (frontiers.get(i).size() > frontiers.get(quarantine).size()) quarantine = i;
            if (frontiers.get(quarantine).isEmpty()) break;
            walls += perimeters.get(quarantine);
            for (long cell : regions.get(quarantine)) {
                int r = (int) (cell >> 32), c = (int) cell;
                isInfected[r][c] = -1;
            }
            for (int index = 0; index < frontiers.size(); index++) {
                if (index == quarantine) continue;
                for (long cell : frontiers.get(index)) {
                    int r = (int) (cell >> 32), c = (int) cell;
                    isInfected[r][c] = 1;
                }
            }
        }
        return walls;
    }
}
