// LeetCode 3787 - Find Diameter Endpoints Of A Tree
// https://leetcode.com/problems/find_diameter_endpoints_of_a_tree/

import java.util.ArrayList;
import java.util.List;

class Solution {
    private List<Integer>[] g;
    private int n;

    public String findSpecialNodes(int n, int[][] edges) {
        this.n = n;
        g = newList(n);
        for (int[] e : edges) {
            g[e[0]].add(e[1]);
            g[e[1]].add(e[0]);
        }
        int[] r0 = bfs(0);
        int a = r0[0];
        int[] r1 = bfs(a);
        int b = r1[0];
        int[] dist1 = java.util.Arrays.copyOfRange(r1, 1, n + 1);
        int[] r2 = bfs(b);
        int[] dist2 = java.util.Arrays.copyOfRange(r2, 1, n + 1);
        int d = dist1[b];
        char[] ans = new char[n];
        java.util.Arrays.fill(ans, '0');
        for (int i = 0; i < n; i++) {
            if (dist1[i] == d || dist2[i] == d) ans[i] = '1';
        }
        return new String(ans);
    }

    // returns [far, dist0, dist1, ...]
    private int[] bfs(int start) {
        int[] dist = new int[n];
        java.util.Arrays.fill(dist, -1);
        dist[start] = 0;
        List<Integer> q = new ArrayList<>();
        q.add(start);
        int far = start;
        for (int head = 0; head < q.size(); head++) {
            int u = q.get(head);
            if (dist[u] > dist[far]) far = u;
            for (int v : g[u]) {
                if (dist[v] == -1) {
                    dist[v] = dist[u] + 1;
                    q.add(v);
                }
            }
        }
        int[] out = new int[n + 1];
        out[0] = far;
        System.arraycopy(dist, 0, out, 1, n);
        return out;
    }

    @SuppressWarnings("unchecked")
    private List<Integer>[] newList(int n) {
        List<Integer>[] g = (List<Integer>[]) new List[n];
        for (int i = 0; i < n; i++) g[i] = new ArrayList<>();
        return g;
    }
}
