// LeetCode 0291 - Word Pattern II
// https://leetcode.com/problems/word-pattern-ii/

#include <string>
#include <unordered_map>

class Solution {
    bool backtrack(
        const std::string& pattern,
        const std::string& s,
        int patternIndex,
        int stringIndex,
        std::unordered_map<char, std::string>& charToWord,
        std::unordered_map<std::string, char>& wordToChar
    ) {
        if (patternIndex == static_cast<int>(pattern.size())) {
            return stringIndex == static_cast<int>(s.size());
        }

        char ch = pattern[patternIndex];
        if (charToWord.count(ch)) {
            const std::string& word = charToWord[ch];
            if (s.compare(stringIndex, word.size(), word) != 0) {
                return false;
            }
            return backtrack(pattern, s, patternIndex + 1, stringIndex + static_cast<int>(word.size()),
                             charToWord, wordToChar);
        }

        for (int end = stringIndex + 1; end <= static_cast<int>(s.size()); end++) {
            std::string word = s.substr(stringIndex, end - stringIndex);
            if (wordToChar.count(word)) {
                continue;
            }
            charToWord[ch] = word;
            wordToChar[word] = ch;
            if (backtrack(pattern, s, patternIndex + 1, end, charToWord, wordToChar)) {
                return true;
            }
            charToWord.erase(ch);
            wordToChar.erase(word);
        }
        return false;
    }

public:
    bool wordPatternMatch(std::string pattern, std::string s) {
        std::unordered_map<char, std::string> charToWord;
        std::unordered_map<std::string, char> wordToChar;
        return backtrack(pattern, s, 0, 0, charToWord, wordToChar);
    }
};
