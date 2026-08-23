// LeetCode 2810 - Faulty Keyboard
// https://leetcode.com/problems/faulty-keyboard/

#include <algorithm>
#include <string>

class Solution {
public:
    std::string finalString(std::string s) {
        std::string b;
        for (char c : s) {
            if (c == 'i') std::reverse(b.begin(), b.end());
            else b.push_back(c);
        }
        return b;
    }
};
