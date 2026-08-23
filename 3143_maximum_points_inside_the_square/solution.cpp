// LeetCode 3143 - Maximum Points Inside the Square
// https://leetcode.com/problems/maximum-points-inside-the-square/

#include <vector>
#include <string>
#include <map>
#include <algorithm>
#include <cmath>

class Solution {
public:
    int maxPointsInsideSquare(std::vector<std::vector<int>>& points, std::string s) {
        std::map<int, std::vector<int>> g;
        for (int i = 0; i < (int)points.size(); i++) {
            int key = std::max({points[i][0], -points[i][0], points[i][1], -points[i][1]});
            g[key].push_back(i);
        }
        bool vis[26] = {};
        int ans = 0;
        for (auto& [k, idx] : g) {
            for (int i : idx) {
                int j = s[i] - 'a';
                if (vis[j]) return ans;
                vis[j] = true;
            }
            ans += (int)idx.size();
        }
        return ans;
    }
};
