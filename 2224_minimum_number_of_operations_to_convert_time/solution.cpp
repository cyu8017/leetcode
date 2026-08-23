// LeetCode 2224 - Minimum Number of Operations to Convert Time
// https://leetcode.com/problems/minimum-number-of-operations-to-convert-time/

#include <string>

class Solution {
public:
    int convertTime(std::string current, std::string correct) {
        auto toMin = [](const std::string& t) {
            return (t[0] - '0') * 600 + (t[1] - '0') * 60 + (t[3] - '0') * 10 + (t[4] - '0');
        };
        int diff = toMin(correct) - toMin(current);
        int ans = 0;
        for (int step : {60, 15, 5, 1}) {
            ans += diff / step;
            diff %= step;
        }
        return ans;
    }
};
