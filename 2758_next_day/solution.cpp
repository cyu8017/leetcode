// LeetCode 2758 - Next Day
// https://leetcode.com/problems/next-day/
// JS Date stand-in using civil-day arithmetic.

#include <cstdio>
#include <string>

class Solution {
public:
    std::string nextDay(std::string date) {
        int y, m, d;
        if (sscanf(date.c_str(), "%d-%d-%d", &y, &m, &d) != 3) return date;
        auto isLeap = [](int yy) { return (yy % 4 == 0 && yy % 100 != 0) || (yy % 400 == 0); };
        int mdays[] = {0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
        if (isLeap(y)) mdays[2] = 29;
        d++;
        if (d > mdays[m]) { d = 1; m++; }
        if (m > 12) { m = 1; y++; }
        char buf[16];
        snprintf(buf, sizeof(buf), "%04d-%02d-%02d", y, m, d);
        return std::string(buf);
    }
};
