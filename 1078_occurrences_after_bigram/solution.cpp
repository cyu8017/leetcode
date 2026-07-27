// LeetCode 1078 - Occurrences After Bigram
// https://leetcode.com/problems/occurrences-after-bigram/

#include <sstream>
#include <string>
#include <vector>

class Solution {
public:
    std::vector<std::string> findOcurrences(std::string text, std::string first, std::string second) {
        std::istringstream iss(text);
        std::vector<std::string> words;
        std::string word;
        while (iss >> word) {
            words.push_back(word);
        }
        std::vector<std::string> ans;
        for (size_t i = 0; i + 2 < words.size(); ++i) {
            if (words[i] == first && words[i + 1] == second) {
                ans.push_back(words[i + 2]);
            }
        }
        return ans;
    }
};
