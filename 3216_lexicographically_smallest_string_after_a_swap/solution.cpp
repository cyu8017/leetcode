// LeetCode 3216 - Lexicographically Smallest String After a Swap
// https://leetcode.com/problems/lexicographically-smallest-string-after-a-swap/

#include <string>

class Solution {
public:
    std::string getSmallestString(std::string s) {
        int n = (int)s.size();
        for (int i = 1; i < n; i++) {
            unsigned char a = s[i - 1], b = s[i];
            if (a > b && a % 2 == b % 2) {
                std::swap(s[i - 1], s[i]);
                return s;
            }
        }
        return s;
    }
};
