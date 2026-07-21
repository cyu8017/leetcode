// LeetCode 1859 - Sorting the Sentence
// https://leetcode.com/problems/sorting-the-sentence/

#include <sstream>
#include <string>
#include <vector>

class Solution {
public:
    std::string sortSentence(std::string s) {
        std::istringstream stream(s);
        std::vector<std::string> tokens;
        std::string token;
        while (stream >> token) {
            tokens.push_back(token);
        }
        std::vector<std::string> ordered(tokens.size());
        for (const std::string& t : tokens) {
            int position = t.back() - '1';
            ordered[position] = t.substr(0, t.size() - 1);
        }
        std::string result;
        for (int i = 0; i < static_cast<int>(ordered.size()); i++) {
            if (i) result += ' ';
            result += ordered[i];
        }
        return result;
    }
};
