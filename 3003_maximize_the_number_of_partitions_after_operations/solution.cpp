// LeetCode 3003 - Maximize the Number of Partitions After Operations
// https://leetcode.com/problems/maximize-the-number-of-partitions-after-operations/

#include <algorithm>
#include <string>
#include <unordered_map>

class Solution {
    static int popcount(unsigned x) { return __builtin_popcount(x); }
public:
    int maxPartitionsAfterOperations(std::string s, int k) {
        int n = (int)s.size();
        std::unordered_map<long long, int> memo;
        auto key = [](int i, int cur, int t) -> long long {
            return ((long long)i << 32) | ((long long)cur << 1) | t;
        };
        auto dfs = [&](auto&& self, int i, int cur, int t) -> int {
            if (i >= n) return 1;
            long long kkey = key(i, cur, t);
            if (auto it = memo.find(kkey); it != memo.end()) return it->second;
            int v = 1 << (s[i] - 'a');
            int nxt = cur | v;
            int ans;
            if (popcount((unsigned)nxt) > k) ans = self(self, i + 1, v, t) + 1;
            else ans = self(self, i + 1, nxt, t);
            if (t > 0) {
                for (int j = 0; j < 26; j++) {
                    nxt = cur | (1 << j);
                    if (popcount((unsigned)nxt) > k)
                        ans = std::max(ans, self(self, i + 1, 1 << j, 0) + 1);
                    else
                        ans = std::max(ans, self(self, i + 1, nxt, 0));
                }
            }
            return memo[kkey] = ans;
        };
        return dfs(dfs, 0, 0, 1);
    }
};
