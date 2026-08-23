// LeetCode 3547 - Maximum Sum of Edge Values in a Graph
// https://leetcode.com/problems/maximum-sum-of-edge-values-in-a-graph/

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

class Solution {
    long calc(int left, int right, boolean isCycle) {
        int w0 = right, w1 = right;
        long score = 0;
        for (int value = right - 1; value >= left; value--) {
            score += 1L * w0 * value;
            w0 = w1;
            w1 = value;
        }
        if (isCycle) score += 1L * w0 * w1;
        return score;
    }

    public long maxScore(int n, int[][] edges) {
        @SuppressWarnings("unchecked")
        List<Integer>[] graph = new ArrayList[n];
        for (int i = 0; i < n; i++) graph[i] = new ArrayList<>();
        for (int[] e : edges) {
            graph[e[0]].add(e[1]);
            graph[e[1]].add(e[0]);
        }
        boolean[] seen = new boolean[n];
        List<Integer> cycleSizes = new ArrayList<>();
        List<Integer> pathSizes = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            if (seen[i]) continue;
            List<Integer> comp = getComp(i, graph, seen);
            boolean allDeg2 = true;
            for (int u : comp) if (graph[u].size() != 2) { allDeg2 = false; break; }
            if (allDeg2) cycleSizes.add(comp.size());
            else if (comp.size() > 1) pathSizes.add(comp.size());
        }
        long ans = 0;
        int curN = n;
        for (int cs : cycleSizes) {
            ans += calc(curN - cs + 1, curN, true);
            curN -= cs;
        }
        pathSizes.sort(Collections.reverseOrder());
        for (int ps : pathSizes) {
            ans += calc(curN - ps + 1, curN, false);
            curN -= ps;
        }
        return ans;
    }

    List<Integer> getComp(int start, List<Integer>[] graph, boolean[] seen) {
        List<Integer> comp = new ArrayList<>();
        comp.add(start);
        seen[start] = true;
        for (int i = 0; i < comp.size(); i++) {
            for (int v : graph[comp.get(i)]) {
                if (!seen[v]) { seen[v] = true; comp.add(v); }
            }
        }
        return comp;
    }
}
