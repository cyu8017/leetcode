// LeetCode 2264 - Largest 3-Same-Digit Number in String
// https://leetcode.com/problems/largest-3-same-digit-number-in-string/

#include <string>

class Solution {
public:
    std::string largestGoodInteger(std::string num) {
        std::string best;
        for (size_t i = 0; i + 2 < num.size(); ++i) {
            if (num[i] == num[i + 1] && num[i] == num[i + 2]) {
                std::string cand = num.substr(i, 3);
                if (cand > best) best = cand;
            }
        }
        return best;
    }
};
