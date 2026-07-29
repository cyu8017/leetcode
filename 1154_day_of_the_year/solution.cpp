// LeetCode 1154 - Day of the Year
// https://leetcode.com/problems/day-of-the-year/

#include <string>

class Solution {
public:
    int dayOfYear(std::string date) {
        int year = std::stoi(date.substr(0, 4));
        int month = std::stoi(date.substr(5, 2));
        int day = std::stoi(date.substr(8, 2));
        bool leap = year % 4 == 0 && (year % 100 != 0 || year % 400 == 0);
        int days[] = {31, leap ? 29 : 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
        int ans = day;
        for (int i = 0; i < month - 1; ++i) ans += days[i];
        return ans;
    }
};
