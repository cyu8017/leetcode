// LeetCode 0527 - Word Abbreviation
// https://leetcode.com/problems/word-abbreviation/

#include <string>
#include <unordered_map>
#include <vector>

class Solution {
    static std::string abbreviate(const std::string& word, int prefix) {
        if (prefix + 2 >= static_cast<int>(word.size())) {
            return word;
        }
        const int middle = static_cast<int>(word.size()) - prefix - 1;
        const std::string candidate =
            word.substr(0, prefix) + std::to_string(middle) + word.back();
        return candidate.size() < word.size() ? candidate : word;
    }

public:
    std::vector<std::string> wordsAbbreviation(std::vector<std::string>& words) {
        std::vector<int> prefixes(words.size(), 1);
        bool changed = true;

        while (changed) {
            changed = false;
            std::unordered_map<std::string, std::vector<int>> groups;
            for (size_t index = 0; index < words.size(); ++index) {
                groups[abbreviate(words[index], prefixes[index])].push_back(static_cast<int>(index));
            }
            for (const auto& entry : groups) {
                if (entry.second.size() > 1) {
                    changed = true;
                    for (const int index : entry.second) {
                        ++prefixes[index];
                    }
                }
            }
        }

        std::vector<std::string> result;
        result.reserve(words.size());
        for (size_t index = 0; index < words.size(); ++index) {
            result.push_back(abbreviate(words[index], prefixes[index]));
        }
        return result;
    }
};
