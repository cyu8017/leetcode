// LeetCode 0472 - Concatenated Words
// https://leetcode.com/problems/concatenated-words/

#include <algorithm>
#include <string>
#include <unordered_set>
#include <vector>

class Solution {
    bool canForm(const std::string& word, const std::unordered_set<std::string>& dictionary) {
        if (word.empty()) {
            return true;
        }
        const int length = static_cast<int>(word.size());
        std::vector<bool> dp(length + 1, false);
        dp[0] = true;
        for (int end = 1; end <= length; ++end) {
            for (int start = 0; start < end; ++start) {
                if (dp[start] && dictionary.count(word.substr(start, end - start))) {
                    dp[end] = true;
                    break;
                }
            }
        }
        return dp[length];
    }

public:
    std::vector<std::string> findAllConcatenatedWordsInADict(std::vector<std::string>& words) {
        std::sort(words.begin(), words.end(), [](const std::string& a, const std::string& b) {
            return a.size() < b.size();
        });

        std::unordered_set<std::string> wordSet(words.begin(), words.end());
        std::vector<std::string> result;
        for (const std::string& word : words) {
            wordSet.erase(word);
            if (canForm(word, wordSet)) {
                result.push_back(word);
            }
            wordSet.insert(word);
        }
        return result;
    }
};
