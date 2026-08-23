// LeetCode 0408 - Valid Word Abbreviation
// https://leetcode.com/problems/valid-word-abbreviation/

#include <cctype>
#include <string>

class Solution {
public:
    bool validWordAbbreviation(string word, string abbr) {
        int wordIndex = 0;
        int abbrIndex = 0;

        while (wordIndex < static_cast<int>(word.size()) && abbrIndex < static_cast<int>(abbr.size())) {
            if (isdigit(abbr[abbrIndex])) {
                if (abbr[abbrIndex] == '0') {
                    return false;
                }

                int number = 0;
                while (abbrIndex < static_cast<int>(abbr.size()) && isdigit(abbr[abbrIndex])) {
                    number = number * 10 + (abbr[abbrIndex] - '0');
                    ++abbrIndex;
                }
                wordIndex += number;
            } else {
                if (word[wordIndex] != abbr[abbrIndex]) {
                    return false;
                }
                ++wordIndex;
                ++abbrIndex;
            }
        }

        return wordIndex == static_cast<int>(word.size()) && abbrIndex == static_cast<int>(abbr.size());
    }
};
