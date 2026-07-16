// LeetCode 0389 - Find the Difference
// https://leetcode.com/problems/find-the-difference/

#include <string>

class Solution {
public:
    char findTheDifference(std::string s, std::string t) {
        int xorValue = 0;

        for (char ch : s) {
            xorValue ^= ch;
        }
        for (char ch : t) {
            xorValue ^= ch;
        }

        return static_cast<char>(xorValue);
    }
};
