// LeetCode 3607 - Power Grid Maintenance
// https://leetcode.com/problems/power-grid-maintenance/

#include <algorithm>
#include <unordered_map>
#include <vector>

class Solution {
public:
    std::vector<int> processQueries(int c, std::vector<std::vector<int>>& connections, std::vector<std::vector<int>>& queries) {
        std::vector<int> parent(c + 1);
        for (int i = 0; i <= c; i++) parent[i] = i;
        auto find = [&](auto&& self, int x) -> int {
            return parent[x] == x ? x : parent[x] = self(self, parent[x]);
        };
        auto unite = [&](int a, int b) {
            int ra = find(find, a), rb = find(find, b);
            if (ra != rb) {
                if (ra < rb) parent[rb] = ra;
                else parent[ra] = rb;
            }
        };
        for (auto& e : connections) unite(e[0], e[1]);
        std::vector<bool> online(c + 1, true);
        std::unordered_map<int, std::vector<int>> comp;
        for (int i = 1; i <= c; i++) comp[find(find, i)].push_back(i);
        for (auto& [_, ids] : comp) std::sort(ids.begin(), ids.end());
        std::unordered_map<int, int> ptr;
        std::vector<int> ans;
        for (auto& q : queries) {
            int t = q[0], x = q[1];
            if (t == 2) {
                online[x] = false;
                continue;
            }
            if (online[x]) {
                ans.push_back(x);
                continue;
            }
            int r = find(find, x);
            auto& ids = comp[r];
            while (ptr[r] < (int)ids.size() && !online[ids[ptr[r]]]) ptr[r]++;
            ans.push_back(ptr[r] < (int)ids.size() ? ids[ptr[r]] : -1);
        }
        return ans;
    }
};
