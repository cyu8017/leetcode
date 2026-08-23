// LeetCode 1904 - The Number of Full Rounds You Have Played
// https://leetcode.com/problems/the-number-of-full-rounds-you-have-played/

#include <algorithm>
#include <string>

class Solution {
public:
    int numberOfRounds(std::string loginTime, std::string logoutTime) {
        auto toMin = [](const std::string& t) {
            return std::stoi(t.substr(0, 2)) * 60 + std::stoi(t.substr(3, 2));
        };
        int start = toMin(loginTime), end = toMin(logoutTime);
        if (end < start) end += 24 * 60;
        start = (start + 14) / 15 * 15;
        end = end / 15 * 15;
        return std::max(0, (end - start) / 15);
    }
};
