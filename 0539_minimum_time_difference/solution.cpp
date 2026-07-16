// LeetCode 0539 - Minimum Time Difference
// https://leetcode.com/problems/minimum-time-difference/

#include <algorithm>
#include <string>
#include <vector>

class Solution {
    static int toMinutes(const std::string& time) {
        const int hour = std::stoi(time.substr(0, 2));
        const int minute = std::stoi(time.substr(3, 2));
        return hour * 60 + minute;
    }

public:
    int findMinDifference(std::vector<std::string>& timePoints) {
        std::vector<int> minutes;
        minutes.reserve(timePoints.size());
        for (const std::string& time : timePoints) {
            minutes.push_back(toMinutes(time));
        }
        std::sort(minutes.begin(), minutes.end());

        int best = minutes.back() - minutes.front();
        for (size_t index = 1; index < minutes.size(); ++index) {
            best = std::min(best, minutes[index] - minutes[index - 1]);
        }
        return std::min(best, 24 * 60 - minutes.back() + minutes.front());
    }
};
