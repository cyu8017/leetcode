// LeetCode 1016 - Binary String With Substrings Representing 1 To N
// https://leetcode.com/problems/binary-string-with-substrings-representing-1-to-n/

#include <algorithm>
#include <string>

class Solution {
    std::string toBin(int x) {
        std::string s;
        while (x) {
            s.push_back(static_cast<char>('0' + (x & 1)));
            x >>= 1;
        }
        std::reverse(s.begin(), s.end());
        return s;
    }

public:
    bool queryString(std::string s, int n) {
        for (int i = n; i > n / 2; --i) {
            if (s.find(toBin(i)) == std::string::npos) return false;
        }
        return true;
    }
};

