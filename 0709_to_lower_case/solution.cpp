// LeetCode 0709 - To Lower Case
// https://leetcode.com/problems/to-lower-case/

#include <string>

class Solution {
public:
    std::string toLowerCase(std::string s) {
        for (char& ch : s) {
            if (ch >= 'A' && ch <= 'Z') {
                ch = static_cast<char>(ch + 32);
            }
        }
        return s;
    }
};
