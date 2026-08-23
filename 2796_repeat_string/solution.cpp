// LeetCode 2796 - Repeat String
// https://leetcode.com/problems/repeat-string/
// JS-only problem; C++ stand-in.

#include <string>

class Solution {
public:
    std::string replicate(std::string str, int times) {
        if (times <= 0) return "";
        std::string out;
        out.reserve(str.size() * times);
        for (int i = 0; i < times; i++) out += str;
        return out;
    }
};
