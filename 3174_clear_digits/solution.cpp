// LeetCode 3174 - Clear Digits
// https://leetcode.com/problems/clear-digits/

#include <string>

class Solution {
public:
    std::string clearDigits(std::string s) {
        std::string stk;
        for (char c : s) {
            if (c >= '0' && c <= '9') stk.pop_back();
            else stk.push_back(c);
        }
        return stk;
    }
};
