// LeetCode 3031 - Minimum Time to Revert Word to Initial State II
// https://leetcode.com/problems/minimum-time-to-revert-word-to-initial-state-ii/

#include <string>
#include <vector>

class Solution {
    struct Hashing {
        std::vector<long long> p, h;
        long long mod;
        Hashing(const std::string& word, long long base, long long mod_) : mod(mod_) {
            int n = (int)word.size();
            p.assign(n + 1, 0);
            h.assign(n + 1, 0);
            p[0] = 1;
            for (int i = 1; i <= n; i++) {
                p[i] = p[i - 1] * base % mod;
                h[i] = (h[i - 1] * base + (word[i - 1] - 'a')) % mod;
            }
        }
        long long query(int l, int r) {
            return (h[r] - h[l - 1] * p[r - l + 1] % mod + mod) % mod;
        }
    };
public:
    int minimumTimeToInitialState(std::string word, int k) {
        Hashing hashing(word, 13331, 998244353);
        int n = (int)word.size();
        for (int i = k; i < n; i += k)
            if (hashing.query(1, n - i) == hashing.query(i + 1, n)) return i / k;
        return (n + k - 1) / k;
    }
};
