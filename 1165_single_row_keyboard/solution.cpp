// LeetCode 1165 - Single-Row Keyboard
// https://leetcode.com/problems/single-row-keyboard/

#include <cmath>
#include <string>
#include <unordered_map>

class Solution {
public:
    int calculateTime(std::string keyboard, std::string word) {
        std::unordered_map<char, int> pos;
        for (int i = 0; i < static_cast<int>(keyboard.size()); ++i) pos[keyboard[i]] = i;
        int ans = 0, prev = 0;
        for (char ch : word) {
            ans += std::abs(pos[ch] - prev);
            prev = pos[ch];
        }
        return ans;
    }
};
