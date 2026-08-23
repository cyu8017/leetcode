// LeetCode 2000 - Reverse Prefix of Word
// https://leetcode.com/problems/reverse-prefix-of-word/

#include <string>
#include <algorithm>

class Solution {
public:
    std::string reversePrefix(std::string word, char ch) {
        auto pos = word.find(ch);
        if (pos == std::string::npos) {
            return word;
        }
        std::reverse(word.begin(), word.begin() + static_cast<std::ptrdiff_t>(pos) + 1);
        return word;
    }
};
