// LeetCode 2734 - Lexicographically Smallest String After Substring Operation
// https://leetcode.com/problems/lexicographically-smallest-string-after-substring-operation/

#include <string>

class Solution {
public:
    std::string smallestString(std::string s) {
        int n = (int)s.size(), i = 0;
        while (i < n && s[i] == 'a') i++;
        if (i == n) { s[n - 1] = 'z'; return s; }
        while (i < n && s[i] != 'a') { s[i]--; i++; }
        return s;
    }
};
