// LeetCode 0065 - Valid Number
// https://leetcode.com/problems/valid-number/

#include <cctype>
#include <string>

class Solution {
public:
    bool isNumber(std::string s) {
        bool seenDigit = false;
        bool seenDot = false;
        bool seenExp = false;

        for (int i = 0; i < static_cast<int>(s.size()); ++i) {
            char ch = s[i];

            if (std::isdigit(static_cast<unsigned char>(ch))) {
                seenDigit = true;
            } else if (ch == '+' || ch == '-') {
                if (i > 0 && s[i - 1] != 'e' && s[i - 1] != 'E') {
                    return false;
                }
            } else if (ch == 'e' || ch == 'E') {
                if (seenExp || !seenDigit) {
                    return false;
                }
                seenExp = true;
                seenDigit = false;
                seenDot = false;
            } else if (ch == '.') {
                if (seenDot || seenExp) {
                    return false;
                }
                seenDot = true;
            } else {
                return false;
            }
        }

        return seenDigit;
    }
};
