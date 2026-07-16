// LeetCode 0320 - Generalized Abbreviation
// https://leetcode.com/problems/generalized-abbreviation/

#include <string>
#include <vector>

class Solution {
    void backtrack(
        const std::string& word,
        int index,
        std::string path,
        int count,
        std::vector<std::string>& result
    ) {
        if (index == static_cast<int>(word.size())) {
            result.push_back(path + (count ? std::to_string(count) : ""));
            return;
        }
        backtrack(word, index + 1, path, count + 1, result);
        std::string nextPath = path + (count ? std::to_string(count) : "") + word[index];
        backtrack(word, index + 1, nextPath, 0, result);
    }

public:
    std::vector<std::string> generateAbbreviations(std::string word) {
        std::vector<std::string> result;
        backtrack(word, 0, "", 0, result);
        return result;
    }
};
