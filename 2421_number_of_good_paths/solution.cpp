// LeetCode 2421 - Number of Good Paths
// https://leetcode.com/problems/number-of-good-paths/

#include <algorithm>
#include <unordered_map>
#include <vector>

class Solution {
public:
    int numberOfGoodPaths(std::vector<int>& vals, std::vector<std::vector<int>>& edges) {
        int n = (int)vals.size();
        std::vector<std::vector<int>> g(n);
        for (auto& e : edges) {
            g[e[0]].push_back(e[1]);
            g[e[1]].push_back(e[0]);
        }
        std::vector<int> parent(n), size(n, 1);
        for (int i = 0; i < n; i++) parent[i] = i;
        auto find = [&](auto&& self, int x) -> int {
            if (parent[x] != x) parent[x] = self(self, parent[x]);
            return parent[x];
        };
        std::vector<int> nodes(n);
        for (int i = 0; i < n; i++) nodes[i] = i;
        std::sort(nodes.begin(), nodes.end(), [&](int a, int b) { return vals[a] < vals[b]; });
        int ans = n;
        for (int i = 0; i < n; ) {
            int j = i;
            while (j < n && vals[nodes[j]] == vals[nodes[i]]) j++;
            for (int k = i; k < j; k++) {
                int u = nodes[k];
                for (int v : g[u]) {
                    if (vals[v] <= vals[u]) {
                        int ru = find(find, u), rv = find(find, v);
                        if (ru != rv) {
                            parent[ru] = rv;
                            size[rv] += size[ru];
                        }
                    }
                }
            }
            std::unordered_map<int, int> freq;
            for (int k = i; k < j; k++) freq[find(find, nodes[k])]++;
            for (auto& [_, c] : freq) ans += c * (c - 1) / 2;
            i = j;
        }
        return ans;
    }
};
