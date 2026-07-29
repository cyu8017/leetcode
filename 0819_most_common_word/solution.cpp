// LeetCode 0819 - Most Common Word
// https://leetcode.com/problems/most-common-word/

#include <cctype>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>

class Solution {
public:
    std::string mostCommonWord(std::string paragraph, std::vector<std::string>& banned) {
        std::unordered_set<std::string> bannedSet(banned.begin(), banned.end());
        std::unordered_map<std::string, int> counts;
        std::string word;
        std::string best;
        int bestCount = 0;
        auto flush = [&]() {
            if (!word.empty()) {
                if (!bannedSet.count(word)) {
                    int c = ++counts[word];
                    if (c > bestCount) {
                        bestCount = c;
                        best = word;
                    }
                }
                word.clear();
            }
        };
        for (char ch : paragraph) {
            if (std::isalpha(static_cast<unsigned char>(ch))) {
                word.push_back(static_cast<char>(std::tolower(static_cast<unsigned char>(ch))));
            } else {
                flush();
            }
        }
        flush();
        return best;
    }
};
