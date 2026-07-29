// LeetCode 1578 - Minimum Time to Make Rope Colorful
// https://leetcode.com/problems/minimum-time-to-make-rope-colorful/

#include <algorithm>
#include <string>
#include <vector>

class Solution {
public:
    int minCost(std::string colors, std::vector<int>& neededTime) {
        int answer = 0;
        int maximum = 0;
        for (int i = 0; i < static_cast<int>(neededTime.size()); ++i) {
            const int cost = neededTime[i];
            if (i && colors[i] != colors[i - 1]) {
                maximum = 0;
            }
            answer += std::min(maximum, cost);
            maximum = std::max(maximum, cost);
        }
        return answer;
    }
};
