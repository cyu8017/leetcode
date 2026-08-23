// LeetCode 2486 - Append Characters to String to Make Subsequence
// https://leetcode.com/problems/append-characters-to-string-to-make-subsequence/

#include <string>

class Solution {
public:
    int appendCharacters(std::string s, std::string t) {
        int j = 0;
        for (int i = 0; i < (int)s.size() && j < (int)t.size(); i++) {
            if (s[i] == t[j]) j++;
        }
        return (int)t.size() - j;
    }
};
