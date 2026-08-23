// LeetCode 3531 - Count Covered Buildings
// https://leetcode.com/problems/count-covered-buildings/

#include <vector>
#include <unordered_map>
#include <algorithm>

class Solution {
public:
    int countCoveredBuildings(int n, std::vector<std::vector<int>>& buildings) {
        std::unordered_map<int, std::vector<int>> g1, g2;
        for (auto& b : buildings) {
            g1[b[0]].push_back(b[1]);
            g2[b[1]].push_back(b[0]);
        }
        for (auto& [_, list] : g1) std::sort(list.begin(), list.end());
        for (auto& [_, list] : g2) std::sort(list.begin(), list.end());
        int ans = 0;
        for (auto& b : buildings) {
            int x = b[0], y = b[1];
            auto& l1 = g1[x];
            auto& l2 = g2[y];
            if (l2.front() < x && x < l2.back() && l1.front() < y && y < l1.back()) ans++;
        }
        return ans;
    }
};
