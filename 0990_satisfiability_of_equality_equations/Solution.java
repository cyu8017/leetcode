// LeetCode 0990 - Satisfiability of Equality Equations
// https://leetcode.com/problems/satisfiability-of-equality-equations/

class Solution {
    private int[] parent;

    public boolean equationsPossible(String[] equations) {
        parent = new int[26];
        for (int i = 0; i < 26; i++) parent[i] = i;
        for (String eq : equations) {
            if (eq.charAt(1) == '=') parent[find(eq.charAt(0) - 'a')] = find(eq.charAt(3) - 'a');
        }
        for (String eq : equations) {
            if (eq.charAt(1) == '!' && find(eq.charAt(0) - 'a') == find(eq.charAt(3) - 'a')) return false;
        }
        return true;
    }

    private int find(int x) {
        return parent[x] == x ? x : (parent[x] = find(parent[x]));
    }
}
