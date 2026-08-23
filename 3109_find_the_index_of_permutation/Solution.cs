// LeetCode 3109 - Find the Index of Permutation
// https://leetcode.com/problems/find-the-index-of-permutation/

public class Solution {
    class BIT {
        int n;
        int[] c;
        public BIT(int n_) { n = n_; c = new int[n_ + 1]; }
        public void Update(int x, int delta) { for (; x <= n; x += x & -x) c[x] += delta; }
        public int Query(int x) { int s = 0; for (; x > 0; x -= x & -x) s += c[x]; return s; }
    }

    public int GetPermutationIndex(int[] perm) {
        const int Mod = 1000000007;
        int n = perm.Length;
        var tree = new BIT(n + 1);
        int[] f = new int[n];
        f[0] = 1;
        for (int i = 1; i < n; i++) f[i] = (int)((long)f[i - 1] * i % Mod);
        long ans = 0;
        for (int i = 0; i < n; i++) {
            int x = perm[i];
            int cnt = x - 1 - tree.Query(x);
            ans = (ans + (long)cnt * f[n - 1 - i]) % Mod;
            tree.Update(x, 1);
        }
        return (int)ans;
    }
}
