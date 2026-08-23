// LeetCode 3109 - Find the Index of Permutation
// https://leetcode.com/problems/find-the-index-of-permutation/

class Solution {
    static class BIT {
        int n;
        int[] c;
        BIT(int n_) { n = n_; c = new int[n_ + 1]; }
        void update(int x, int delta) { for (; x <= n; x += x & -x) c[x] += delta; }
        int query(int x) { int s = 0; for (; x > 0; x -= x & -x) s += c[x]; return s; }
    }

    public int getPermutationIndex(int[] perm) {
        final int MOD = 1_000_000_007;
        int n = perm.length;
        BIT tree = new BIT(n + 1);
        int[] f = new int[n];
        f[0] = 1;
        for (int i = 1; i < n; i++) f[i] = (int) ((long) f[i - 1] * i % MOD);
        long ans = 0;
        for (int i = 0; i < n; i++) {
            int x = perm[i];
            int cnt = x - 1 - tree.query(x);
            ans = (ans + (long) cnt * f[n - 1 - i]) % MOD;
            tree.update(x, 1);
        }
        return (int) ans;
    }
}
