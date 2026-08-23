// LeetCode 0520 - Detect Capital
// https://leetcode.com/problems/detect-capital/

#include <cctype>
#include <string>

class Solution {
public:
    bool detectCapitalUse(std::string word) {
        bool allUpper = true;
        bool allLower = true;
        for (const unsigned char ch : word) {
            if (std::isupper(ch)) {
                allLower = false;
            } else {
                allUpper = false;
            }
        }
        if (allUpper || allLower) {
            return true;
        }
        for (size_t index = 1; index < word.size(); ++index) {
            if (std::isupper(static_cast<unsigned char>(word[index]))) {
                return false;
            }
        }
        return std::isupper(static_cast<unsigned char>(word[0]));
    }
};
