// LeetCode 3493 - Properties Graph
// https://leetcode.com/problems/properties-graph/

using System.Collections.Generic;

public class Solution {
    public int NumberOfComponents(int[][] properties, int k) {
        int n = properties.Length;
        var sets = new HashSet<int>[n];
        for (int i = 0; i < n; i++) {
            sets[i] = new HashSet<int>();
            foreach (int v in properties[i]) sets[i].Add(v);
        }
        int[] parent = new int[n];
        for (int i = 0; i < n; i++) parent[i] = i;
        int Find(int x) {
            if (parent[x] != x) parent[x] = Find(parent[x]);
            return parent[x];
        }
        void Unite(int a, int b) {
            int ra = Find(a), rb = Find(b);
            if (ra != rb) parent[ra] = rb;
        }
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                int cnt = 0;
                foreach (int v in sets[i]) if (sets[j].Contains(v)) cnt++;
                if (cnt >= k) Unite(i, j);
            }
        }
        var comp = new HashSet<int>();
        for (int i = 0; i < n; i++) comp.Add(Find(i));
        return comp.Count;
    }
}
