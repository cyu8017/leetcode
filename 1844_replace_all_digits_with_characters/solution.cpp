// LeetCode 1844 - Replace All Digits with Characters
// https://leetcode.com/problems/replace-all-digits-with-characters/

#include <string>

class Solution {
public:
    std::string replaceDigits(std::string s) {
        for (size_t i = 1; i < s.size(); i += 2) {
            s[i] = static_cast<char>(s[i - 1] + (s[i] - '0'));
        }
        return s;
    }
};
