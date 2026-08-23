// LeetCode 0681 - Next Closest Time
// https://leetcode.com/problems/next-closest-time/

#include <set>
#include <string>

class Solution {
public:
    std::string nextClosestTime(std::string time) {
        std::set<char> digits = {time[0], time[1], time[3], time[4]};
        const int start = std::stoi(time.substr(0, 2)) * 60 + std::stoi(time.substr(3, 2));
        for (int delta = 1; delta <= 24 * 60; ++delta) {
            const int mins = (start + delta) % (24 * 60);
            const int hh = mins / 60;
            const int mm = mins % 60;
            char candidate[5];
            candidate[0] = static_cast<char>('0' + hh / 10);
            candidate[1] = static_cast<char>('0' + hh % 10);
            candidate[2] = static_cast<char>('0' + mm / 10);
            candidate[3] = static_cast<char>('0' + mm % 10);
            candidate[4] = '\0';
            bool valid = true;
            for (int i = 0; i < 4; ++i) {
                if (!digits.count(candidate[i])) {
                    valid = false;
                    break;
                }
            }
            if (valid) {
                std::string result;
                result += candidate[0];
                result += candidate[1];
                result += ':';
                result += candidate[2];
                result += candidate[3];
                return result;
            }
        }
        return time;
    }
};
