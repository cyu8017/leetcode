// LeetCode 1768 - Merge Strings Alternately
// https://leetcode.com/problems/merge-strings-alternately/

#include <string>

class Solution {
public:
    std::string mergeAlternately(std::string word1, std::string word2) {
        std::string out;
        out.reserve(word1.size() + word2.size());
        size_t i = 0;
        size_t j = 0;
        while (i < word1.size() || j < word2.size()) {
            if (i < word1.size()) {
                out.push_back(word1[i++]);
            }
            if (j < word2.size()) {
                out.push_back(word2[j++]);
            }
        }
        return out;
    }
};
