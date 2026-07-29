// LeetCode 1938 - Maximum Genetic Difference Query
#include <functional>
#include <vector>

struct TrieNode {
    TrieNode* child[2] = {nullptr, nullptr};
    int cnt = 0;
};

class Solution {
public:
    std::vector<int> maxGeneticDifference(std::vector<int>& parents, std::vector<std::vector<int>>& queries) {
        int n = (int)parents.size();
        std::vector<std::vector<int>> children(n);
        int root = 0;
        for (int i = 0; i < n; i++) {
            if (parents[i] == -1) root = i;
            else children[parents[i]].push_back(i);
        }
        std::vector<std::vector<std::pair<int, int>>> qmap(n);
        for (int i = 0; i < (int)queries.size(); i++) {
            qmap[queries[i][0]].push_back({i, queries[i][1]});
        }
        std::vector<int> ans(queries.size());
        TrieNode* trieRoot = new TrieNode();
        const int BITS = 17;
        auto trieUpdate = [&](int num, int delta) {
            TrieNode* node = trieRoot;
            for (int b = BITS; b >= 0; b--) {
                int bit = (num >> b) & 1;
                if (!node->child[bit]) node->child[bit] = new TrieNode();
                node = node->child[bit];
                node->cnt += delta;
            }
        };
        auto trieMaxXor = [&](int num) {
            TrieNode* node = trieRoot;
            int res = 0;
            for (int b = BITS; b >= 0; b--) {
                int bit = (num >> b) & 1;
                int want = 1 - bit;
                if (node->child[want] && node->child[want]->cnt > 0) {
                    res |= 1 << b;
                    node = node->child[want];
                } else {
                    node = node->child[bit];
                }
            }
            return res;
        };
        std::function<void(int)> dfs = [&](int u) {
            trieUpdate(u, 1);
            for (auto [qi, val] : qmap[u]) ans[qi] = trieMaxXor(val);
            for (int v : children[u]) dfs(v);
            trieUpdate(u, -1);
        };
        dfs(root);
        return ans;
    }
};
