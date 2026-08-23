// LeetCode 0288 - Unique Word Abbreviation
// https://leetcode.com/problems/unique-word-abbreviation/

#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>

class ValidWordAbbr {
    std::unordered_map<std::string, std::unordered_set<std::string>> groups;

    static std::string abbreviate(const std::string& word) {
        if (word.size() <= 2) {
            return word;
        }
        return word.front() + std::to_string(word.size() - 2) + word.back();
    }

public:
    ValidWordAbbr(const std::vector<std::string>& dictionary) {
        for (const std::string& word : dictionary) {
            groups[abbreviate(word)].insert(word);
        }
    }

    bool isUnique(const std::string& word) {
        const std::string key = abbreviate(word);
        const auto iterator = groups.find(key);
        if (iterator == groups.end()) {
            return true;
        }
        const auto& words = iterator->second;
        return words.size() == 1 && words.count(word) == 1;
    }
};
