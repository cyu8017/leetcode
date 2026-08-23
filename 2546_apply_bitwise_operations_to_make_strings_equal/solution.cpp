// LeetCode 2546 - Apply Bitwise Operations to Make Strings Equal
// https://leetcode.com/problems/apply-bitwise-operations-to-make-strings-equal/

#include <string>

class Solution {
public:
    bool makeStringsEqual(std::string s, std::string target) {
        bool has1s = false, has1t = false;
        for (size_t i = 0; i < s.size(); ++i) {
            if (s[i] == '1') has1s = true;
            if (target[i] == '1') has1t = true;
        }
        return has1s == has1t;
    }
};
