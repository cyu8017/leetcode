// LeetCode 2777 - Date Range Generator
// https://leetcode.com/problems/date-range-generator/
// JS generator stand-in using civil-day arithmetic.

#include <cstdio>
#include <string>
#include <vector>

class Solution {
public:
    std::vector<std::string> dateRangeGenerator(std::string start, std::string end, int step) {
        int y, m, d, ey, em, ed;
        if (sscanf(start.c_str(), "%d-%d-%d", &y, &m, &d) != 3) return {};
        if (sscanf(end.c_str(), "%d-%d-%d", &ey, &em, &ed) != 3) return {};
        auto isLeap = [](int yy) { return (yy % 4 == 0 && yy % 100 != 0) || (yy % 400 == 0); };
        auto addDays = [&](int& yy, int& mm, int& dd, int days) {
            int mdays[] = {0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
            while (days--) {
                if (isLeap(yy)) mdays[2] = 29; else mdays[2] = 28;
                dd++;
                if (dd > mdays[mm]) { dd = 1; mm++; }
                if (mm > 12) { mm = 1; yy++; }
            }
        };
        auto cmp = [&]() {
            if (y != ey) return y < ey;
            if (m != em) return m < em;
            return d <= ed;
        };
        std::vector<std::string> ans;
        while (cmp()) {
            char buf[16];
            snprintf(buf, sizeof(buf), "%04d-%02d-%02d", y, m, d);
            ans.push_back(buf);
            addDays(y, m, d, step);
        }
        return ans;
    }
};
