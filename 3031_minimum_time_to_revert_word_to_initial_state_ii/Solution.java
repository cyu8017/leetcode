// LeetCode 3031 - Minimum Time to Revert Word to Initial State II
// https://leetcode.com/problems/minimum-time-to-revert-word-to-initial-state-ii/

class Solution {
    class Hashing {
        long[] p, h;
        long mod;
        Hashing(String word, long bas, long mod_) {
            mod = mod_;
            int n = word.length();
            p = new long[n + 1];
            h = new long[n + 1];
            p[0] = 1;
            for (int i = 1; i <= n; i++) {
                p[i] = p[i - 1] * bas % mod;
                h[i] = (h[i - 1] * bas + (word.charAt(i - 1) - 'a')) % mod;
            }
        }
        long query(int l, int r) {
            return (h[r] - h[l - 1] * p[r - l + 1] % mod + mod) % mod;
        }
    }

    public int minimumTimeToInitialState(String word, int k) {
        Hashing hashing = new Hashing(word, 13331, 998244353);
        int n = word.length();
        for (int i = k; i < n; i += k)
            if (hashing.query(1, n - i) == hashing.query(i + 1, n)) return i / k;
        return (n + k - 1) / k;
    }
}
