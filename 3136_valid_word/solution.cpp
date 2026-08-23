// LeetCode 3136 - Valid Word
// https://leetcode.com/problems/valid-word/

#include <string>
#include <cctype>

class Solution {
public:
    bool isValid(std::string word) {
        if ((int)word.size() < 3) return false;
        bool hasVowel = false, hasConsonant = false;
        bool vs[26] = {};
        for (char c : std::string("aeiou")) vs[c - 'a'] = true;
        for (char c : word) {
            if (std::isalpha((unsigned char)c)) {
                char lower = (char)std::tolower((unsigned char)c);
                if (vs[lower - 'a']) hasVowel = true;
                else hasConsonant = true;
            } else if (!std::isdigit((unsigned char)c)) {
                return false;
            }
        }
        return hasVowel && hasConsonant;
    }
};
