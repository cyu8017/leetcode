// LeetCode 0171 - Excel Sheet Column Number
// https://leetcode.com/problems/excel-sheet-column-number/

#include <string>

class Solution {
public:
    int titleToNumber(std::string columnTitle) {
        int result = 0;
        for (char ch : columnTitle) {
            result = result * 26 + (ch - 'A' + 1);
        }
        return result;
    }
};