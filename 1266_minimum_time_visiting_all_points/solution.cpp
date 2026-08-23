// LeetCode 1266 - Minimum Time Visiting All Points
// https://leetcode.com/problems/minimum-time-visiting-all-points/

#include <algorithm>
#include <cstdlib>
#include <vector>

class Solution {
public:
    int minTimeToVisitAllPoints(std::vector<std::vector<int>>& points) {
        int answer = 0;
        for (int i = 1; i < static_cast<int>(points.size()); ++i) {
            answer += std::max(std::abs(points[i][0] - points[i - 1][0]),
                               std::abs(points[i][1] - points[i - 1][1]));
        }
        return answer;
    }
};
