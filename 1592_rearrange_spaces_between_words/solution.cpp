// LeetCode 1592 - Rearrange Spaces Between Words
// https://leetcode.com/problems/rearrange-spaces-between-words/

#include <sstream>
#include <string>
#include <vector>

class Solution {
public:
    std::string reorderSpaces(std::string text) {
        std::vector<std::string> words;
        std::istringstream iss(text);
        std::string word;
        while (iss >> word) {
            words.push_back(word);
        }
        int spaces = 0;
        for (char ch : text) {
            if (ch == ' ') {
                ++spaces;
            }
        }
        if (words.size() == 1) {
            return words[0] + std::string(spaces, ' ');
        }
        const int between = spaces / static_cast<int>(words.size() - 1);
        const int trailing = spaces % static_cast<int>(words.size() - 1);
        std::string result = words[0];
        for (size_t i = 1; i < words.size(); ++i) {
            result += std::string(between, ' ');
            result += words[i];
        }
        result += std::string(trailing, ' ');
        return result;
    }
};
