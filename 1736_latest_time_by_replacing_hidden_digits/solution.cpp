// LeetCode 1736 - Latest Time by Replacing Hidden Digits
// https://leetcode.com/problems/latest-time-by-replacing-hidden-digits/

#include <string>

class Solution {
public:
    std::string maximumTime(std::string time) {
        if (time[0] == '?') {
            time[0] = (std::string("0123?").find(time[1]) != std::string::npos) ? '2' : '1';
        }
        if (time[1] == '?') {
            time[1] = time[0] == '2' ? '3' : '9';
        }
        if (time[3] == '?') {
            time[3] = '5';
        }
        if (time[4] == '?') {
            time[4] = '9';
        }
        return time;
    }
};
