// LeetCode 1042 - Flower Planting With No Adjacent
// https://leetcode.com/problems/flower-planting-with-no-adjacent/

import java.util.ArrayList;
import java.util.List;

class Solution {
    public int[] gardenNoAdj(int n, int[][] paths) {
        List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i <= n; i++) graph.add(new ArrayList<>());
        for (int[] p : paths) {
            graph.get(p[0]).add(p[1]);
            graph.get(p[1]).add(p[0]);
        }
        int[] ans = new int[n + 1];
        for (int garden = 1; garden <= n; garden++) {
            boolean[] used = new boolean[5];
            for (int nei : graph.get(garden)) used[ans[nei]] = true;
            for (int c = 1; c <= 4; c++) {
                if (!used[c]) {
                    ans[garden] = c;
                    break;
                }
            }
        }
        int[] res = new int[n];
        System.arraycopy(ans, 1, res, 0, n);
        return res;
    }
}
