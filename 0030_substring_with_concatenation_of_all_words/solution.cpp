// LeetCode 0030 - Substring with Concatenation of All Words
// https://leetcode.com/problems/substring-with-concatenation-of-all-words/

#include <algorithm>
#include <string>
#include <unordered_map>
#include <vector>

class Solution {
public:
    std::vector<int> findSubstring(std::string s, std::vector<std::string>& words) {
        std::vector<int> result;
        if (words.empty() || s.empty()) {
            return result;
        }

        int wordLen = static_cast<int>(words[0].size());
        int wordCount = static_cast<int>(words.size());
        std::unordered_map<std::string, int> need;
        for (const std::string& word : words) {
            need[word]++;
        }

        for (int start = 0; start < wordLen; start++) {
            int left = start;
            std::unordered_map<std::string, int> counts;
            int used = 0;

            for (int right = start; right <= static_cast<int>(s.size()) - wordLen; right += wordLen) {
                std::string word = s.substr(right, wordLen);
                if (!need.count(word)) {
                    counts.clear();
                    used = 0;
                    left = right + wordLen;
                    continue;
                }

                counts[word]++;
                used++;
                while (counts[word] > need[word]) {
                    std::string leftWord = s.substr(left, wordLen);
                    counts[leftWord]--;
                    used--;
                    left += wordLen;
                }

                if (used == wordCount) {
                    result.push_back(left);
                }
            }
        }

        std::sort(result.begin(), result.end());
        return result;
    }
};
