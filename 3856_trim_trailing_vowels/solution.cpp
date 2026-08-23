// LeetCode 3856 - Trim Trailing Vowels
// https://leetcode.com/problems/trim-trailing-vowels/

#include <string>

class Solution {
public:
    std::string trimTrailingVowels(std::string s) {
        int i = (int)s.size() - 1;
        auto isVowel = [](char c) {
            return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
        };
        while (i >= 0 && isVowel(s[i])) i--;
        return s.substr(0, i + 1);
    }
};
