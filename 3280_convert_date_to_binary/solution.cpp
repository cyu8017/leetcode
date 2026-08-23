// LeetCode 3280 - Convert Date to Binary
// https://leetcode.com/problems/convert-date-to-binary/

#include <sstream>
#include <string>

class Solution {
    std::string toBinary(int v) {
        if (v == 0) return "0";
        std::string s;
        while (v > 0) {
            s.insert(s.begin(), char('0' + (v & 1)));
            v >>= 1;
        }
        return s;
    }

public:
    std::string convertDateToBinary(std::string date) {
        int y, m, d;
        char c;
        std::stringstream ss(date);
        ss >> y >> c >> m >> c >> d;
        return toBinary(y) + "-" + toBinary(m) + "-" + toBinary(d);
    }
};
