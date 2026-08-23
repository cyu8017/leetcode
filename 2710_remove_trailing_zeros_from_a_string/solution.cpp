// LeetCode 2710 - Remove Trailing Zeros From a String
// https://leetcode.com/problems/remove-trailing-zeros-from-a-string/

#include <string>

class Solution {
public:
    std::string removeTrailingZeros(std::string num) {
        while (!num.empty() && num.back() == '0') num.pop_back();
        return num;
    }
};
