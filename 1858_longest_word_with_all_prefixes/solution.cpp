// LeetCode 1858 - Longest Word With All Prefixes
// https://leetcode.com/problems/longest-word-with-all-prefixes/

#include <string>
#include <unordered_set>
#include <vector>

class Solution {
public:
    std::string longestWord(std::vector<std::string>& words) {
        std::unordered_set<std::string> wordSet(words.begin(), words.end());
        std::string best;
        for (const std::string& word : words) {
            std::string prefix = word;
            bool valid = true;
            while (!prefix.empty()) {
                if (!wordSet.count(prefix)) {
                    valid = false;
                    break;
                }
                prefix.pop_back();
            }
            if (valid && (word.size() > best.size() || (word.size() == best.size() && word < best))) {
                best = word;
            }
        }
        return best;
    }
};
