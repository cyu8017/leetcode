// LeetCode 3841 - Palindromic Path Queries in a Tree
// https://leetcode.com/problems/palindromic-path-queries-in-a-tree/

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    private int[] bit;
    private int n;
    private int[] parent, depth, size, heavy, head, position;
    private List<Integer>[] graph;

    public boolean[] palindromicPathQueries(int n, int[][] edges, String s, String[] queries) {
        this.n = n;
        @SuppressWarnings("unchecked")
        List<Integer>[] g = new ArrayList[n];
        graph = g;
        for (int i = 0; i < n; i++) graph[i] = new ArrayList<>();
        for (int[] edge : edges) {
            graph[edge[0]].add(edge[1]);
            graph[edge[1]].add(edge[0]);
        }
        parent = new int[n];
        depth = new int[n];
        Arrays.fill(parent, -2);
        parent[0] = -1;
        List<Integer> order = new ArrayList<>();
        order.add(0);
        for (int i = 0; i < order.size(); i++) {
            int u = order.get(i);
            for (int v : graph[u]) {
                if (parent[v] == -2) {
                    parent[v] = u;
                    depth[v] = depth[u] + 1;
                    order.add(v);
                }
            }
        }
        size = new int[n];
        heavy = new int[n];
        Arrays.fill(heavy, -1);
        for (int i = n - 1; i >= 0; i--) {
            int u = order.get(i);
            size[u] = 1;
            for (int v : graph[u]) {
                if (parent[v] == u) {
                    size[u] += size[v];
                    if (heavy[u] == -1 || size[v] > size[heavy[u]]) heavy[u] = v;
                }
            }
        }
        head = new int[n];
        position = new int[n];
        List<int[]> stack = new ArrayList<>();
        stack.add(new int[] { 0, 0 });
        int nextPosition = 0;
        while (!stack.isEmpty()) {
            int[] chain = stack.remove(stack.size() - 1);
            for (int u = chain[0]; u != -1; u = heavy[u]) {
                head[u] = chain[1];
                position[u] = nextPosition++;
                for (int v : graph[u]) {
                    if (parent[v] == u && v != heavy[u]) stack.add(new int[] { v, v });
                }
            }
        }
        bit = new int[n + 1];
        char[] current = s.toCharArray();
        for (int node = 0; node < n; node++) update(position[node], 1 << (current[node] - 'a'));
        List<Boolean> answer = new ArrayList<>();
        for (String query : queries) {
            String[] parts = query.split(" ");
            String op = parts[0];
            int node = Integer.parseInt(parts[1]);
            if (op.equals("update")) {
                char newCharacter = parts[2].charAt(0);
                int delta = (1 << (current[node] - 'a')) ^ (1 << (newCharacter - 'a'));
                update(position[node], delta);
                current[node] = newCharacter;
            } else {
                int other = Integer.parseInt(parts[2]);
                int mask = pathMask(node, other);
                answer.add((mask & (mask - 1)) == 0);
            }
        }
        boolean[] out = new boolean[answer.size()];
        for (int i = 0; i < answer.size(); i++) out[i] = answer.get(i);
        return out;
    }

    private void update(int index, int value) {
        for (index++; index <= n; index += index & -index) bit[index] ^= value;
    }

    private int prefix(int index) {
        int result = 0;
        for (; index > 0; index -= index & -index) result ^= bit[index];
        return result;
    }

    private int pathMask(int u, int v) {
        int result = 0;
        while (head[u] != head[v]) {
            if (depth[head[u]] < depth[head[v]]) { int tmp = u; u = v; v = tmp; }
            result ^= prefix(position[u] + 1) ^ prefix(position[head[u]]);
            u = parent[head[u]];
        }
        if (position[u] > position[v]) { int tmp = u; u = v; v = tmp; }
        return result ^ prefix(position[v] + 1) ^ prefix(position[u]);
    }
}
