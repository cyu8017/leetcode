// LeetCode 1182 - Shortest Distance to Target Color
// https://leetcode.com/problems/shortest-distance-to-target-color/

#include <algorithm>
#include <climits>
#include <unordered_map>
#include <vector>

class Solution {
public:
    std::vector<int> shortestDistanceColor(std::vector<int>& colors, std::vector<std::vector<int>>& queries) {
        std::unordered_map<int, std::vector<int>> pos;
        for (int i = 0; i < static_cast<int>(colors.size()); ++i) pos[colors[i]].push_back(i);
        std::vector<int> ans;
        for (const auto& q : queries) {
            int i = q[0], c = q[1];
            if (!pos.count(c)) { ans.push_back(-1); continue; }
            const auto& arr = pos[c];
            auto it = std::lower_bound(arr.begin(), arr.end(), i);
            int best = INT_MAX;
            if (it != arr.end()) best = std::min(best, *it - i);
            if (it != arr.begin()) best = std::min(best, i - *std::prev(it));
            ans.push_back(best == INT_MAX ? -1 : best);
        }
        return ans;
    }
};
