// LeetCode 3887 - Incremental Even-Weighted Cycle Queries
// https://leetcode.com/problems/incremental-even-weighted-cycle-queries/

#include <utility>
#include <vector>

class Solution {
public:
    int countValidEdges(int n, std::vector<std::vector<int>>& edges) {
        std::vector<int> parent(n), size(n, 1), parity(n, 0);
        for (int i = 0; i < n; i++) parent[i] = i;

        auto find = [&](auto&& self, int x) -> std::pair<int, int> {
            if (parent[x] == x) return {x, 0};
            auto [root, p] = self(self, parent[x]);
            parity[x] ^= p;
            parent[x] = root;
            return {root, parity[x]};
        };

        int ans = 0;
        for (auto& e : edges) {
            auto [ru, pu] = find(find, e[0]);
            auto [rv, pv] = find(find, e[1]);
            if (ru == rv) {
                if ((pu ^ pv) == e[2]) ans++;
                continue;
            }
            if (size[ru] < size[rv]) {
                std::swap(ru, rv);
                std::swap(pu, pv);
            }
            parent[rv] = ru;
            parity[rv] = pu ^ pv ^ e[2];
            size[ru] += size[rv];
            ans++;
        }
        return ans;
    }
};
