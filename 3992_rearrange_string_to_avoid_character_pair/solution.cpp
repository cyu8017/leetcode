// LeetCode 3992 - Rearrange String to Avoid Character Pair
// https://leetcode.com/problems/rearrange-string-to-avoid-character-pair/

#include <string>

class Solution {
public:
    std::string rearrangeString(std::string s, char x, char y) {
        (void)x;
        int i = 0;
        for (int j = 0; j < (int)s.size(); j++) {
            if (s[j] == y) {
                std::swap(s[i], s[j]);
                i++;
            }
        }
        return s;
    }
};
