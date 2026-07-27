// LeetCode 1090 - Largest Values From Labels
// https://leetcode.com/problems/largest-values-from-labels/

#include <algorithm>
#include <unordered_map>
#include <vector>

class Solution {
public:
    int largestValsFromLabels(std::vector<int>& values, std::vector<int>& labels, int numWanted,
                              int useLimit) {
        std::vector<std::pair<int, int>> items;
        items.reserve(values.size());
        for (size_t i = 0; i < values.size(); ++i) {
            items.emplace_back(values[i], labels[i]);
        }
        std::sort(items.begin(), items.end(), std::greater<>());
        std::unordered_map<int, int> used;
        int ans = 0;
        int taken = 0;
        for (const auto& [value, label] : items) {
            if (taken == numWanted) {
                break;
            }
            if (used[label] < useLimit) {
                ++used[label];
                ans += value;
                ++taken;
            }
        }
        return ans;
    }
};
