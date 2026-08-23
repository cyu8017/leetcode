// LeetCode 3493 - Properties Graph
// https://leetcode.com/problems/properties-graph/

import java.util.HashSet;
import java.util.Set;

class Solution {
    private int[] parent;

    private int find(int x) {
        if (parent[x] != x) parent[x] = find(parent[x]);
        return parent[x];
    }

    private void unite(int a, int b) {
        int ra = find(a), rb = find(b);
        if (ra != rb) parent[ra] = rb;
    }

    public int numberOfComponents(int[][] properties, int k) {
        int n = properties.length;
        @SuppressWarnings("unchecked")
        Set<Integer>[] sets = new HashSet[n];
        for (int i = 0; i < n; i++) {
            sets[i] = new HashSet<>();
            for (int v : properties[i]) sets[i].add(v);
        }
        parent = new int[n];
        for (int i = 0; i < n; i++) parent[i] = i;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                int cnt = 0;
                for (int v : sets[i]) if (sets[j].contains(v)) cnt++;
                if (cnt >= k) unite(i, j);
            }
        }
        Set<Integer> comp = new HashSet<>();
        for (int i = 0; i < n; i++) comp.add(find(i));
        return comp.size();
    }
}
