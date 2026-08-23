// LeetCode 0524 - Longest Word in Dictionary through Deleting
// https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/

#include <string>
#include <vector>

class Solution {
    static bool isSubsequence(const std::string& word, const std::string& source) {
        size_t index = 0;
        for (const char ch : source) {
            if (index < word.size() && word[index] == ch) {
                ++index;
            }
        }
        return index == word.size();
    }

public:
    std::string findLongestWord(std::string s, std::vector<std::string>& dictionary) {
        std::string best;
        for (const std::string& word : dictionary) {
            if (!isSubsequence(word, s)) {
                continue;
            }
            if (word.size() > best.size() || (word.size() == best.size() && word < best)) {
                best = word;
            }
        }
        return best;
    }
};
