// LeetCode 1163 - Last Substring in Lexicographical Order
// https://leetcode.com/problems/last-substring-in-lexicographical-order/

#include <algorithm>
#include <string>

class Solution {
public:
    std::string lastSubstring(std::string s) {
        int i = 0, j = 1, k = 0, n = static_cast<int>(s.size());
        while (j + k < n) {
            if (s[i + k] == s[j + k]) { ++k; continue; }
            if (s[i + k] > s[j + k]) j = j + k + 1;
            else {
                i = std::max(i + k + 1, j);
                j = i + 1;
            }
            k = 0;
        }
        return s.substr(i);
    }
};
