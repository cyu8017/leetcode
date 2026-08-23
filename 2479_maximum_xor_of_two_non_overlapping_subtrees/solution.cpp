// LeetCode 2479 - Maximum XOR of Two Non-Overlapping Subtrees
// https://leetcode.com/problems/maximum-xor-of-two-non-overlapping-subtrees/

#include <array>
#include <functional>
#include <memory>
#include <vector>

class Solution {
public:
    long long maxXor(int n, std::vector<std::vector<int>>& edges, std::vector<int>& values) {
        std::vector<std::vector<int>> g(n);
        for (auto& e : edges) {
            g[e[0]].push_back(e[1]);
            g[e[1]].push_back(e[0]);
        }
        std::vector<long long> sum(n);
        std::function<long long(int, int)> dfsSum = [&](int u, int p) {
            long long s = values[u];
            for (int v : g[u]) if (v != p) s += dfsSum(v, u);
            return sum[u] = s;
        };
        dfsSum(0, -1);

        struct Trie {
            Trie* child[2] = {nullptr, nullptr};
        };
        Trie* root = new Trie();
        auto insert = [&](long long x) {
            Trie* cur = root;
            for (int b = 46; b >= 0; b--) {
                int bit = (int)((x >> b) & 1);
                if (!cur->child[bit]) cur->child[bit] = new Trie();
                cur = cur->child[bit];
            }
        };
        auto query = [&](long long x) {
            Trie* cur = root;
            if (!cur->child[0] && !cur->child[1]) return 0LL;
            long long ans = 0;
            for (int b = 46; b >= 0; b--) {
                int bit = (int)((x >> b) & 1);
                int want = bit ^ 1;
                if (cur->child[want]) {
                    ans |= 1LL << b;
                    cur = cur->child[want];
                } else if (cur->child[bit]) {
                    cur = cur->child[bit];
                } else {
                    return ans;
                }
            }
            return ans;
        };

        long long ans = 0;
        std::function<void(int, int)> dfs = [&](int u, int p) {
            for (int v : g[u]) {
                if (v == p) continue;
                long long xorv = query(sum[v]);
                if (xorv > ans) ans = xorv;
                dfs(v, u);
                insert(sum[v]);
            }
        };
        dfs(0, -1);
        return ans;
    }
};
