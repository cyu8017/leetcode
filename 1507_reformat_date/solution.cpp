// LeetCode 1507 - Reformat Date
// https://leetcode.com/problems/reformat-date/

#include <cstdio>
#include <sstream>
#include <string>
#include <vector>

class Solution {
public:
    std::string reformatDate(std::string date) {
        static const std::vector<std::string> months = {
            "Jan", "Feb", "Mar", "Apr", "May", "Jun",
            "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"};
        std::istringstream iss(date);
        std::string day, month, year;
        iss >> day >> month >> year;
        int month_num = 0;
        for (int i = 0; i < 12; ++i) {
            if (months[i] == month) {
                month_num = i + 1;
                break;
            }
        }
        const int day_num = std::stoi(day.substr(0, day.size() - 2));
        char buffer[16];
        std::snprintf(buffer, sizeof(buffer), "%s-%02d-%02d", year.c_str(), month_num, day_num);
        return std::string(buffer);
    }
};
