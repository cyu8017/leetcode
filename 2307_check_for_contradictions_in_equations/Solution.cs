// LeetCode 2307 - Check for Contradictions in Equations
// https://leetcode.com/problems/check-for-contradictions-in-equations/

using System;
using System.Collections.Generic;

public class Solution {
    public bool CheckContradictions(IList<IList<string>> equations, double[] values) {
        var parent = new Dictionary<string, string>();
        var weight = new Dictionary<string, double>();
        string Find(string x) {
            if (!parent.ContainsKey(x)) { parent[x] = x; weight[x] = 1; return x; }
            if (parent[x] != x) {
                string p = Find(parent[x]);
                weight[x] *= weight[parent[x]];
                parent[x] = p;
            }
            return parent[x];
        }
        for (int i = 0; i < equations.Count; ++i) {
            string a = equations[i][0], b = equations[i][1];
            string ra = Find(a), rb = Find(b);
            if (ra == rb) {
                if (Math.Abs(weight[a] / weight[b] - values[i]) > 1e-5) return true;
            } else {
                parent[ra] = rb;
                weight[ra] = values[i] * weight[b] / weight[a];
            }
        }
        return false;
    }
}
