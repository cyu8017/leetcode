// LeetCode 0880 - Decoded String at Index
// https://leetcode.com/problems/decoded-string-at-index/

#include <cctype>
#include <string>

class Solution {
public:
    std::string decodeAtIndex(std::string s, int k) {
        long long size = 0;
        for (char ch : s) {
            if (std::isdigit(static_cast<unsigned char>(ch))) {
                size *= ch - '0';
            } else {
                ++size;
            }
        }
        long long kk = k;
        for (int i = static_cast<int>(s.size()) - 1; i >= 0; --i) {
            char ch = s[i];
            kk %= size;
            if (kk == 0 && std::isalpha(static_cast<unsigned char>(ch))) {
                return std::string(1, ch);
            }
            if (std::isdigit(static_cast<unsigned char>(ch))) {
                size /= ch - '0';
            } else {
                --size;
            }
        }
        return "";
    }
};
