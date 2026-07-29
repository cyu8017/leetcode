// LeetCode 1202 - Smallest String With Swaps
// https://leetcode.com/problems/smallest-string-with-swaps/

#include <algorithm>
#include <string>
#include <unordered_map>
#include <vector>

class Solution {
public:
    std::string smallestStringWithSwaps(std::string s, std::vector<std::vector<int>>& pairs) {
        const int n = static_cast<int>(s.size());
        std::vector<int> parent(n);
        for (int i = 0; i < n; ++i) {
            parent[i] = i;
        }
        auto find = [&](int x) {
            while (x != parent[x]) {
                parent[x] = parent[parent[x]];
                x = parent[x];
            }
            return x;
        };
        for (const auto& p : pairs) {
            parent[find(p[0])] = find(p[1]);
        }
        std::unordered_map<int, std::vector<char>> groups;
        for (int i = 0; i < n; ++i) {
            groups[find(i)].push_back(s[i]);
        }
        for (auto& [_, chars] : groups) {
            std::sort(chars.begin(), chars.end(), std::greater<char>());
        }
        for (int i = 0; i < n; ++i) {
            auto& chars = groups[find(i)];
            s[i] = chars.back();
            chars.pop_back();
        }
        return s;
    }
};
