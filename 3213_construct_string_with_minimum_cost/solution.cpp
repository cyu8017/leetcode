// LeetCode 3213 - Construct String with Minimum Cost
// https://leetcode.com/problems/construct-string-with-minimum-cost/

#include <vector>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <algorithm>
#include <climits>

class Solution {
    struct Hashing {
        std::vector<long long> p, h;
        long long mod;
        Hashing(const std::string& word, long long base, long long mod) : mod(mod) {
            int n = (int)word.size();
            p.assign(n + 1, 0);
            h.assign(n + 1, 0);
            p[0] = 1;
            for (int i = 1; i <= n; i++) {
                p[i] = p[i - 1] * base % mod;
                h[i] = (h[i - 1] * base + word[i - 1]) % mod;
            }
        }
        long long query(int l, int r) {
            return (h[r] - h[l - 1] * p[r - l + 1] % mod + mod) % mod;
        }
    };
public:
    int minimumCost(std::string target, std::vector<std::string>& words, std::vector<int>& costs) {
        const long long base = 13331, mod = 998244353;
        const int inf = INT_MAX / 2;
        int n = (int)target.size();
        Hashing hashing(target, base, mod);
        std::vector<int> f(n + 1, inf);
        f[0] = 0;
        std::unordered_set<int> ss;
        for (auto& w : words) ss.insert((int)w.size());
        std::vector<int> lengths(ss.begin(), ss.end());
        std::sort(lengths.begin(), lengths.end());
        std::unordered_map<long long, int> d;
        for (int i = 0; i < (int)words.size(); i++) {
            long long x = 0;
            for (char c : words[i]) x = (x * base + c) % mod;
            auto it = d.find(x);
            if (it == d.end() || costs[i] < it->second) d[x] = costs[i];
        }
        for (int i = 1; i <= n; i++) {
            for (int j : lengths) {
                if (j > i) break;
                long long x = hashing.query(i - j + 1, i);
                auto it = d.find(x);
                if (it != d.end()) f[i] = std::min(f[i], f[i - j] + it->second);
            }
        }
        return f[n] >= inf ? -1 : f[n];
    }
};
