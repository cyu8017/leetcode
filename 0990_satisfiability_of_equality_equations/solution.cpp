// LeetCode 0990 - Satisfiability of Equality Equations
// https://leetcode.com/problems/satisfiability-of-equality-equations/

#include <string>
#include <vector>

class Solution {
public:
    bool equationsPossible(std::vector<std::string>& equations) {
        std::vector<int> parent(26);
        for (int i = 0; i < 26; i++) parent[i] = i;
        auto find = [&](auto&& self, int x) -> int {
            return parent[x] == x ? x : parent[x] = self(self, parent[x]);
        };
        for (const auto& eq : equations) {
            if (eq[1] == '=') parent[find(find, eq[0] - 'a')] = find(find, eq[3] - 'a');
        }
        for (const auto& eq : equations) {
            if (eq[1] == '!' && find(find, eq[0] - 'a') == find(find, eq[3] - 'a')) return false;
        }
        return true;
    }
};
