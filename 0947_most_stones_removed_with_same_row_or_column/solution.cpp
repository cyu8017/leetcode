// LeetCode 0947 - Most Stones Removed with Same Row or Column
// https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/

#include <unordered_map>
#include <unordered_set>
#include <vector>

class Solution {
public:
    int removeStones(std::vector<std::vector<int>>& stones) {
        std::unordered_map<int, int> parent;
        auto find = [&](auto&& self, int x) -> int {
            if (!parent.count(x)) parent[x] = x;
            return parent[x] == x ? x : parent[x] = self(self, parent[x]);
        };
        auto unite = [&](int a, int b) { parent[find(find, a)] = find(find, b); };
        for (auto& s : stones) unite(s[0], ~s[1]);
        std::unordered_set<int> roots;
        for (auto& s : stones) roots.insert(find(find, s[0]));
        return (int)stones.size() - (int)roots.size();
    }
};
