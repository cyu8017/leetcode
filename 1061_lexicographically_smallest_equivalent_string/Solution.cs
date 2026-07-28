// LeetCode 1061 - Lexicographically Smallest Equivalent String
// https://leetcode.com/problems/lexicographically-smallest-equivalent-string/

using System.Text;

public class Solution {
    public string SmallestEquivalentString(string s1, string s2, string baseStr) {
        int[] parent = new int[26];
        for (int i = 0; i < 26; i++) {
            parent[i] = i;
        }

        int Find(int x) {
            while (parent[x] != x) {
                parent[x] = parent[parent[x]];
                x = parent[x];
            }
            return x;
        }

        void Union(int a, int b) {
            int ra = Find(a), rb = Find(b);
            if (ra == rb) {
                return;
            }
            if (ra < rb) {
                parent[rb] = ra;
            } else {
                parent[ra] = rb;
            }
        }

        for (int i = 0; i < s1.Length; i++) {
            Union(s1[i] - 'a', s2[i] - 'a');
        }
        var sb = new StringBuilder(baseStr.Length);
        foreach (char c in baseStr) {
            sb.Append((char)(Find(c - 'a') + 'a'));
        }
        return sb.ToString();
    }
}
