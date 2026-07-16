// LeetCode 0495 - Teemo Attacking
// https://leetcode.com/problems/teemo-attacking/

#include <algorithm>
#include <vector>

class Solution {
public:
    int findPoisonedDuration(std::vector<int>& timeSeries, int duration) {
        if (timeSeries.empty()) {
            return 0;
        }
        int total = duration;
        for (int index = 1; index < static_cast<int>(timeSeries.size()); ++index) {
            total += std::min(duration, timeSeries[index] - timeSeries[index - 1]);
        }
        return total;
    }
};
