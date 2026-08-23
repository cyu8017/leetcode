// LeetCode 3585 - Find Weighted Median Node in Tree
// https://leetcode.com/problems/find-weighted-median-node-in-tree/

import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.Queue;

class Solution {
    public int[] findMedian(int n, int[][] edges, int[][] queries) {
        @SuppressWarnings("unchecked")
        List<int[]>[] g = new ArrayList[n];
        for (int i = 0; i < n; i++) g[i] = new ArrayList<>();
        for (int[] e : edges) {
            g[e[0]].add(new int[] {e[1], e[2]});
            g[e[1]].add(new int[] {e[0], e[2]});
        }
        int[] ans = new int[queries.length];
        for (int qi = 0; qi < queries.length; qi++) {
            int u = queries[qi][0], v = queries[qi][1];
            int[] parent = new int[n], pw = new int[n];
            Arrays.fill(parent, -2);
            parent[u] = -1;
            Queue<Integer> q = new ArrayDeque<>();
            q.add(u);
            while (!q.isEmpty()) {
                int x = q.poll();
                if (x == v) break;
                for (int[] e : g[x]) {
                    if (parent[e[0]] == -2) {
                        parent[e[0]] = x;
                        pw[e[0]] = e[1];
                        q.add(e[0]);
                    }
                }
            }
            List<Integer> nodes = new ArrayList<>();
            nodes.add(v);
            List<Integer> weights = new ArrayList<>();
            int cur = v;
            while (cur != u) {
                weights.add(pw[cur]);
                cur = parent[cur];
                nodes.add(cur);
            }
            Collections.reverse(nodes);
            Collections.reverse(weights);
            int total = 0;
            for (int w : weights) total += w;
            int need = (total + 1) / 2, sum = 0, med = u;
            for (int i = 0; i < weights.size(); i++) {
                sum += weights.get(i);
                med = nodes.get(i + 1);
                if (sum >= need) break;
            }
            ans[qi] = med;
        }
        return ans;
    }
}
