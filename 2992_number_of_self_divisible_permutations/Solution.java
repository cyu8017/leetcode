// LeetCode 2992 - Number of Self-Divisible Permutations
// https://leetcode.com/problems/number-of-self-divisible-permutations/

class Solution {
    private int ans;
    private boolean[] used;
    private int n;

    private static int gcd(int a, int b) {
        while (b != 0) { int t = a % b; a = b; b = t; }
        return a;
    }

    private void dfs(int pos) {
        if (pos > n) {
            ans++;
            return;
        }
        for (int v = 1; v <= n; v++) {
            if (used[v]) continue;
            if (gcd(v, pos) != 1) continue;
            used[v] = true;
            dfs(pos + 1);
            used[v] = false;
        }
    }

    public int selfDivisiblePermutationCount(int n) {
        this.n = n;
        ans = 0;
        used = new boolean[n + 1];
        dfs(1);
        return ans;
    }
}
