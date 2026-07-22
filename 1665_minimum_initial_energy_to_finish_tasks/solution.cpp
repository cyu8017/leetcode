// LeetCode 1665 - Minimum Initial Energy to Finish Tasks
// https://leetcode.com/problems/minimum-initial-energy-to-finish-tasks/

#include <algorithm>
#include <vector>

class Solution {
public:
    int minimumEffort(std::vector<std::vector<int>>& tasks) {
        std::sort(tasks.begin(), tasks.end(), [](const auto& a, const auto& b) {
            return a[1] - a[0] > b[1] - b[0];
        });
        int energy = 0;
        int spent = 0;
        for (const auto& t : tasks) {
            energy = std::max(energy, spent + t[1]);
            spent += t[0];
        }
        return energy;
    }
};
