// LeetCode 0541 - Reverse String II
// https://leetcode.com/problems/reverse-string-ii/

#include <algorithm>
#include <string>

class Solution {
public:
    std::string reverseStr(std::string s, int k) {
        for (int start = 0; start < static_cast<int>(s.size()); start += 2 * k) {
            const int end = std::min(start + k, static_cast<int>(s.size())) - 1;
            std::reverse(s.begin() + start, s.begin() + end + 1);
        }
        return s;
    }
};
