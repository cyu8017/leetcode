// LeetCode 1086 - High Five
// https://leetcode.com/problems/high-five/

#include <algorithm>
#include <map>
#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> highFive(std::vector<std::vector<int>>& items) {
        std::map<int, std::vector<int>> scores;
        for (const auto& item : items) {
            scores[item[0]].push_back(item[1]);
        }
        std::vector<std::vector<int>> ans;
        for (auto& [studentId, vals] : scores) {
            std::sort(vals.begin(), vals.end(), std::greater<>());
            int sum = 0;
            for (int i = 0; i < 5; ++i) {
                sum += vals[i];
            }
            ans.push_back({studentId, sum / 5});
        }
        return ans;
    }
};
