// LeetCode 2259 - Remove Digit From Number to Maximize Result
// https://leetcode.com/problems/remove-digit-from-number-to-maximize-result/

#include <string>

class Solution {
public:
    std::string removeDigit(std::string number, char digit) {
        std::string best;
        for (size_t i = 0; i < number.size(); ++i) {
            if (number[i] == digit) {
                std::string cand = number.substr(0, i) + number.substr(i + 1);
                if (cand > best) best = cand;
            }
        }
        return best;
    }
};
