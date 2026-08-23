// LeetCode 3109 - Find the Index of Permutation
// https://leetcode.com/problems/find-the-index-of-permutation/

#include <vector>

class Solution {
    struct BIT {
        int n;
        std::vector<int> c;
        explicit BIT(int n_) : n(n_), c(n_ + 1, 0) {}
        void update(int x, int delta) { for (; x <= n; x += x & -x) c[x] += delta; }
        int query(int x) { int s = 0; for (; x > 0; x -= x & -x) s += c[x]; return s; }
    };
public:
    int getPermutationIndex(std::vector<int>& perm) {
        const int mod = 1e9 + 7;
        int n = (int)perm.size();
        BIT tree(n + 1);
        std::vector<int> f(n);
        f[0] = 1;
        for (int i = 1; i < n; i++) f[i] = (long long)f[i - 1] * i % mod;
        long long ans = 0;
        for (int i = 0; i < n; i++) {
            int x = perm[i];
            int cnt = x - 1 - tree.query(x);
            ans = (ans + (long long)cnt * f[n - 1 - i]) % mod;
            tree.update(x, 1);
        }
        return (int)ans;
    }
};
