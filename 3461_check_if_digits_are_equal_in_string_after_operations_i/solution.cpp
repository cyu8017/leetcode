// LeetCode 3461 - Check If Digits Are Equal in String After Operations I
// https://leetcode.com/problems/check-if-digits-are-equal-in-string-after-operations-i/

#include <string>
#include <vector>

class Solution {
public:
    bool hasSameDigits(std::string s) {
        std::vector<char> b(s.begin(), s.end());
        while ((int)b.size() > 2) {
            std::vector<char> nb(b.size() - 1);
            for (int i = 0; i + 1 < (int)b.size(); i++) {
                nb[i] = char('0' + (b[i] - '0' + b[i + 1] - '0') % 10);
            }
            b.swap(nb);
        }
        return b[0] == b[1];
    }
};
