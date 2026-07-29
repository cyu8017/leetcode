#include <cstdlib>
#include <string>

class Solution {
    int toDays(const std::string& s) {
        int y = std::stoi(s.substr(0, 4));
        int m = std::stoi(s.substr(5, 2));
        int d = std::stoi(s.substr(8, 2));
        auto isLeap = [](int year) {
            return year % 400 == 0 || (year % 4 == 0 && year % 100 != 0);
        };
        int days = d;
        static int mdays[] = {0,31,28,31,30,31,30,31,31,30,31,30,31};
        for (int i = 1; i < m; ++i) days += mdays[i];
        if (m > 2 && isLeap(y)) ++days;
        for (int year = 1971; year < y; ++year) days += isLeap(year) ? 366 : 365;
        return days;
    }
public:
    int daysBetweenDates(std::string date1, std::string date2) {
        return std::abs(toDays(date1) - toDays(date2));
    }
};
