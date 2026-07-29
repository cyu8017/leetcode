// LeetCode 0720 - Longest Word in Dictionary
// https://leetcode.com/problems/longest-word-in-dictionary/

#include <algorithm>
#include <string>
#include <unordered_set>
#include <vector>

class Solution {
public:
    std::string longestWord(std::vector<std::string>& words) {
        std::sort(words.begin(), words.end());
        std::unordered_set<std::string> built{""};
        std::string best;
        for (const std::string& word : words) {
            if (built.count(word.substr(0, word.size() - 1))) {
                built.insert(word);
                if (word.size() > best.size()) {
                    best = word;
                }
            }
        }
        return best;
    }
};
