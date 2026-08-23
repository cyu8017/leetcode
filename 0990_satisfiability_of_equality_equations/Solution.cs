// LeetCode 0990 - Satisfiability of Equality Equations
// https://leetcode.com/problems/satisfiability-of-equality-equations/

public class Solution {
    public bool EquationsPossible(string[] equations) {
        int[] parent = new int[26];
        for (int i = 0; i < 26; i++) parent[i] = i;
        int Find(int x) {
            return parent[x] == x ? x : parent[x] = Find(parent[x]);
        }
        foreach (var eq in equations) {
            if (eq[1] == '=') parent[Find(eq[0] - 'a')] = Find(eq[3] - 'a');
        }
        foreach (var eq in equations) {
            if (eq[1] == '!' && Find(eq[0] - 'a') == Find(eq[3] - 'a')) return false;
        }
        return true;
    }
}
