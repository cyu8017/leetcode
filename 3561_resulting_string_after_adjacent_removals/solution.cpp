// LeetCode 3561 - Resulting String After Adjacent Removals
// https://leetcode.com/problems/resulting-string-after-adjacent-removals/

#include <cmath>
#include <string>

class Solution {
public:
    std::string resultingString(std::string s) {
        auto isContiguous = [](char a, char b) {
            int x = std::abs(a - b);
            return x == 1 || x == 25;
        };
        std::string stk;
        for (char c : s) {
            if (!stk.empty() && isContiguous(stk.back(), c)) stk.pop_back();
            else stk.push_back(c);
        }
        return stk;
    }
};
