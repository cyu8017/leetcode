// LeetCode 3986 - Number of Elapsed Seconds Between Two Times
// https://leetcode.com/problems/number-of-elapsed-seconds-between-two-times/

#include <string>

class Solution {
    static int toSeconds(const std::string& s) {
        int h = (s[0] - '0') * 10 + (s[1] - '0');
        int m = (s[3] - '0') * 10 + (s[4] - '0');
        int sec = (s[6] - '0') * 10 + (s[7] - '0');
        return h * 3600 + m * 60 + sec;
    }

public:
    int secondsBetweenTimes(std::string startTime, std::string endTime) {
        return toSeconds(endTime) - toSeconds(startTime);
    }
};
