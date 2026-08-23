// LeetCode 2564 - Substring XOR Queries
// https://leetcode.com/problems/substring-xor-queries/

#include <string>
#include <unordered_map>
#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> substringXorQueries(std::string s, std::vector<std::vector<int>>& queries) {
        std::unordered_map<int, std::pair<int, int>> pos;
        int n = (int)s.size();
        for (int i = 0; i < n; ++i) {
            if (s[i] == '0') {
                if (!pos.count(0)) pos[0] = {i, i};
                continue;
            }
            int val = 0;
            for (int j = i; j < n && j < i + 30; ++j) {
                val = val * 2 + (s[j] - '0');
                if (!pos.count(val)) pos[val] = {i, j};
            }
        }
        std::vector<std::vector<int>> ans(queries.size());
        for (size_t i = 0; i < queries.size(); ++i) {
            int need = queries[i][0] ^ queries[i][1];
            if (pos.count(need)) ans[i] = {pos[need].first, pos[need].second};
            else ans[i] = {-1, -1};
        }
        return ans;
    }
};
