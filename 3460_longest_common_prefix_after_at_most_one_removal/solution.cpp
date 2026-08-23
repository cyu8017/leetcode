// LeetCode 3460 - Longest Common Prefix After at Most One Removal
// https://leetcode.com/problems/longest-common-prefix-after-at-most-one-removal/

#include <string>

class Solution {
public:
    int longestCommonPrefix(std::string s, std::string t) {
        int i = 0, j = 0;
        bool removed = false;
        while (i < (int)s.size() && j < (int)t.size()) {
            if (s[i] == t[j]) {
                i++;
                j++;
                continue;
            }
            if (removed) break;
            removed = true;
            i++;
        }
        return j;
    }
};
