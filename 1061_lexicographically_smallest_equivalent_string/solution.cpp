// LeetCode 1061 - Lexicographically Smallest Equivalent String
// https://leetcode.com/problems/lexicographically-smallest-equivalent-string/

#include <numeric>
#include <string>
#include <vector>

class Solution {
public:
    std::string smallestEquivalentString(std::string s1, std::string s2, std::string baseStr) {
        std::vector<int> parent(26);
        std::iota(parent.begin(), parent.end(), 0);

        auto find = [&](int x) {
            while (parent[x] != x) {
                parent[x] = parent[parent[x]];
                x = parent[x];
            }
            return x;
        };

        auto unite = [&](int a, int b) {
            int ra = find(a);
            int rb = find(b);
            if (ra == rb) {
                return;
            }
            if (ra < rb) {
                parent[rb] = ra;
            } else {
                parent[ra] = rb;
            }
        };

        for (size_t i = 0; i < s1.size(); ++i) {
            unite(s1[i] - 'a', s2[i] - 'a');
        }
        std::string ans;
        ans.reserve(baseStr.size());
        for (char c : baseStr) {
            ans.push_back(static_cast<char>(find(c - 'a') + 'a'));
        }
        return ans;
    }
};
