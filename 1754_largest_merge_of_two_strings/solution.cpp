// LeetCode 1754 - Largest Merge Of Two Strings
// https://leetcode.com/problems/largest-merge-of-two-strings/

#include <string>

class Solution {
public:
    std::string largestMerge(std::string word1, std::string word2) {
        size_t i = 0;
        size_t j = 0;
        std::string out;
        while (i < word1.size() && j < word2.size()) {
            if (word1.compare(i, std::string::npos, word2, j, std::string::npos) > 0) {
                out += word1[i];
                i++;
            } else {
                out += word2[j];
                j++;
            }
        }
        out += word1.substr(i);
        out += word2.substr(j);
        return out;
    }
};
