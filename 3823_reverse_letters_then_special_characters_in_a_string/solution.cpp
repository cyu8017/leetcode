// LeetCode 3823 - Reverse Letters Then Special Characters In A String
// https://leetcode.com/problems/reverse-letters-then-special-characters-in-a-string/

#include <cctype>
#include <string>
#include <vector>

class Solution {
public:
    std::string reverseByType(std::string s) {
        std::vector<char> a, b;
        for (char c : s) {
            if ((c >= 'A' && c <= 'Z') || (c >= 'a' && c <= 'z')) a.push_back(c);
            else b.push_back(c);
        }
        int j = (int)a.size(), k = (int)b.size();
        for (int i = 0; i < (int)s.size(); i++) {
            if ((s[i] >= 'A' && s[i] <= 'Z') || (s[i] >= 'a' && s[i] <= 'z')) s[i] = a[--j];
            else s[i] = b[--k];
        }
        return s;
    }
};
