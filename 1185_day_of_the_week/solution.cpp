// LeetCode 1185 - Day of the Week
// https://leetcode.com/problems/day-of-the-week/

#include <string>

class Solution {
public:
    std::string dayOfTheWeek(int day, int month, int year) {
        static const std::string names[] = {
            "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"};
        if (month < 3) { month += 12; --year; }
        int k = year % 100, j = year / 100;
        int h = (day + (13 * (month + 1)) / 5 + k + k / 4 + j / 4 + 5 * j) % 7;
        return names[(h + 6) % 7];
    }
};
