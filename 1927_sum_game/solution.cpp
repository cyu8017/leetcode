// LeetCode 1927 - Sum Game
// https://leetcode.com/problems/sum-game/

#include <string>

class Solution {
public:
    bool sumGame(std::string num) {
        int n = (int)num.size(), half = n / 2;
        auto score = [](const std::string& s) {
            int q = 0, dig = 0;
            for (char c : s) {
                if (c == '?') q++;
                else dig += c - '0';
            }
            return dig * 2 + q * 9;
        };
        return score(num.substr(0, half)) != score(num.substr(half));
    }
};
