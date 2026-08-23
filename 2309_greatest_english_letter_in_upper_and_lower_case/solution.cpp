// LeetCode 2309 - Greatest English Letter in Upper and Lower Case
// https://leetcode.com/problems/greatest-english-letter-in-upper-and-lower-case/

#include <string>
#include <array>

class Solution {
public:
    std::string greatestLetter(std::string s) {
        std::array<bool, 26> lower{}, upper{};
        for (char c : s) {
            if (c >= 'a' && c <= 'z') lower[c - 'a'] = true;
            else upper[c - 'A'] = true;
        }
        for (int i = 25; i >= 0; --i)
            if (lower[i] && upper[i]) return std::string(1, char('A' + i));
        return "";
    }
};
