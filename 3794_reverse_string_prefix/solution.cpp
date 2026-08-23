// LeetCode 3794 - Reverse String Prefix
// https://leetcode.com/problems/reverse-string-prefix/

#include <algorithm>
#include <string>

class Solution {
public:
    std::string reversePrefix(std::string s, int k) {
        std::reverse(s.begin(), s.begin() + k);
        return s;
    }
};
