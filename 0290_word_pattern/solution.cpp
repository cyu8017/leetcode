// LeetCode 0290 - Word Pattern
// https://leetcode.com/problems/word-pattern/

#include <sstream>
#include <string>
#include <unordered_map>
#include <vector>

class Solution {
public:
    bool wordPattern(std::string pattern, std::string s) {
        std::istringstream stream(s);
        std::vector<std::string> words;
        std::string word;
        while (stream >> word) {
            words.push_back(word);
        }
        if (pattern.size() != words.size()) {
            return false;
        }

        std::unordered_map<char, std::string> charToWord;
        std::unordered_map<std::string, char> wordToChar;
        for (size_t index = 0; index < pattern.size(); index++) {
            char ch = pattern[index];
            const std::string& currentWord = words[index];
            if (charToWord.count(ch)) {
                if (charToWord[ch] != currentWord) {
                    return false;
                }
            } else {
                if (wordToChar.count(currentWord)) {
                    return false;
                }
                charToWord[ch] = currentWord;
                wordToChar[currentWord] = ch;
            }
        }
        return true;
    }
};
