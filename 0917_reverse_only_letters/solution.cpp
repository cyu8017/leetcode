// LeetCode 0917 - Reverse Only Letters
// https://leetcode.com/problems/reverse-only-letters/

#include <cctype>
#include <string>

class Solution {
public:
    std::string reverseOnlyLetters(std::string s) {
        int i = 0, j = (int)s.size() - 1;
        while (i < j) {
            while (i < j && !std::isalpha(static_cast<unsigned char>(s[i]))) i++;
            while (i < j && !std::isalpha(static_cast<unsigned char>(s[j]))) j--;
            std::swap(s[i], s[j]);
            i++;
            j--;
        }
        return s;
    }
};
