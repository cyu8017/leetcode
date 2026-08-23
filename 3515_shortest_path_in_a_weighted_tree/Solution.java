// LeetCode 3515 - Shortest Path in a Weighted Tree
// https://leetcode.com/problems/shortest-path-in-a-weighted-tree/

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

@SuppressWarnings("unchecked")
class Solution {
    int[] inT, outT, dist, parent, bit;
    int time, n;
    List<int[]>[] g;

    void dfs(int u, int p) {
        inT[u] = time++;
        for (int[] e : g[u]) {
            int to = e[0], w = e[1];
            if (to == p) continue;
            parent[to] = u;
            dist[to] = dist[u] + w;
            dfs(to, u);
        }
        outT[u] = time - 1;
    }

    void add(int i, int v) {
        for (; i <= n; i += i & -i) bit[i] += v;
    }

    void rangeAdd(int l, int r, int v) {
        add(l + 1, v);
        add(r + 2, -v);
    }

    int point(int i) {
        int s = 0;
        for (i++; i > 0; i -= i & -i) s += bit[i];
        return s;
    }

    public int[] treeQueries(int n, int[][] edges, int[][] queries) {
        this.n = n;
        g = new ArrayList[n + 1];
        for (int i = 0; i <= n; i++) g[i] = new ArrayList<>();
        Map<Long, Integer> weight = new HashMap<>();
        for (int[] e : edges) {
            int u = e[0], v = e[1], w = e[2];
            g[u].add(new int[] {v, w});
            g[v].add(new int[] {u, w});
            int a = Math.min(u, v), b = Math.max(u, v);
            weight.put(((long) a << 32) | b, w);
        }
        inT = new int[n + 1];
        outT = new int[n + 1];
        dist = new int[n + 1];
        parent = new int[n + 1];
        time = 0;
        dfs(1, 0);
        bit = new int[n + 2];
        for (int i = 1; i <= n; i++) rangeAdd(inT[i], inT[i], dist[i]);
        List<Integer> ans = new ArrayList<>();
        for (int[] q : queries) {
            if (q[0] == 1) {
                int u = q[1], v = q[2], nw = q[3];
                int a = Math.min(u, v), b = Math.max(u, v);
                long key = ((long) a << 32) | b;
                int ow = weight.get(key);
                int delta = nw - ow;
                weight.put(key, nw);
                int child = (parent[u] == v) ? u : v;
                rangeAdd(inT[child], outT[child], delta);
            } else {
                ans.add(point(inT[q[1]]));
            }
        }
        return ans.stream().mapToInt(Integer::intValue).toArray();
    }
}
