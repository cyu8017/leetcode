// LeetCode 3031 - Minimum Time to Revert Word to Initial State II
// https://leetcode.com/problems/minimum-time-to-revert-word-to-initial-state-ii/

public class Solution {
    class Hashing {
        long[] p, h;
        long mod;
        public Hashing(string word, long bas, long mod_) {
            mod = mod_;
            int n = word.Length;
            p = new long[n + 1];
            h = new long[n + 1];
            p[0] = 1;
            for (int i = 1; i <= n; i++) {
                p[i] = p[i - 1] * bas % mod;
                h[i] = (h[i - 1] * bas + (word[i - 1] - 'a')) % mod;
            }
        }
        public long Query(int l, int r) {
            return (h[r] - h[l - 1] * p[r - l + 1] % mod + mod) % mod;
        }
    }

    public int MinimumTimeToInitialState(string word, int k) {
        var hashing = new Hashing(word, 13331, 998244353);
        int n = word.Length;
        for (int i = k; i < n; i += k)
            if (hashing.Query(1, n - i) == hashing.Query(i + 1, n)) return i / k;
        return (n + k - 1) / k;
    }
}
