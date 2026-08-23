// LeetCode 0006 - Zigzag Conversion
// https://leetcode.com/problems/zigzag-conversion/

#include <string>
#include <vector>

class Solution {
public:
    std::string convert(std::string s, int numRows) {
        if (numRows == 1 || numRows >= static_cast<int>(s.size())) {
            return s;
        }

        std::vector<std::string> rows(numRows);
        int index = 0;
        int step = 1;

        for (char ch : s) {
            rows[index] += ch;
            if (index == 0) {
                step = 1;
            } else if (index == numRows - 1) {
                step = -1;
            }
            index += step;
        }

        std::string result;
        for (const std::string& row : rows) {
            result += row;
        }
        return result;
    }
};
