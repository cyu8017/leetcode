// LeetCode 0678 - Valid Parenthesis String
// https://leetcode.com/problems/valid-parenthesis-string/

#include <algorithm>
#include <string>

class Solution {
public:
    bool checkValidString(std::string s) {
        int lo = 0;
        int hi = 0;
        for (char ch : s) {
            if (ch == '(') {
                ++lo;
                ++hi;
            } else if (ch == ')') {
                lo = std::max(lo - 1, 0);
                --hi;
                if (hi < 0) {
                    return false;
                }
            } else {
                lo = std::max(lo - 1, 0);
                ++hi;
            }
        }
        return lo == 0;
    }
};
