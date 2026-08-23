// LeetCode 0839 - Similar String Groups
// https://leetcode.com/problems/similar-string-groups/

using System.Collections.Generic;

public class Solution {
    public int NumSimilarGroups(string[] strs) {
        int n = strs.Length;
        int[] parent = new int[n];
        for (int i = 0; i < n; i++) parent[i] = i;
        int Find(int x) {
            while (parent[x] != x) { parent[x] = parent[parent[x]]; x = parent[x]; }
            return x;
        }
        bool Similar(string a, string b) {
            var diff = new List<int>();
            for (int i = 0; i < a.Length; i++) {
                if (a[i] != b[i]) {
                    diff.Add(i);
                    if (diff.Count > 2) return false;
                }
            }
            return diff.Count == 0 || (diff.Count == 2 && a[diff[0]] == b[diff[1]] && a[diff[1]] == b[diff[0]]);
        }
        int groups = n;
        for (int i = 0; i < n; i++)
            for (int j = i + 1; j < n; j++)
                if (Similar(strs[i], strs[j])) {
                    int pi = Find(i), pj = Find(j);
                    if (pi != pj) { parent[pi] = pj; groups--; }
                }
        return groups;
    }
}
