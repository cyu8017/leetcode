// LeetCode 3612 - Process String with Special Operations I
// https://leetcode.com/problems/process-string-with-special-operations-i/

#include <algorithm>
#include <cctype>
#include <string>

class Solution {
public:
    std::string processStr(std::string s) {
        std::string result;
        for (char c : s) {
            if (std::isalpha((unsigned char)c)) result.push_back(c);
            else if (c == '*') {
                if (!result.empty()) result.pop_back();
            } else if (c == '#') result += result;
            else if (c == '%') std::reverse(result.begin(), result.end());
        }
        return result;
    }
};
