// LeetCode 0676 - Implement Magic Dictionary
// https://leetcode.com/problems/implement-magic-dictionary/

#include <string>
#include <vector>

class MagicDictionary {
    std::vector<std::string> words_;

public:
    MagicDictionary() = default;

    void buildDict(std::vector<std::string> dictionary) { words_ = std::move(dictionary); }

    bool search(std::string searchWord) {
        for (const std::string& word : words_) {
            if (word.size() != searchWord.size()) {
                continue;
            }
            int diff = 0;
            for (std::size_t i = 0; i < word.size(); ++i) {
                if (word[i] != searchWord[i]) {
                    ++diff;
                }
            }
            if (diff == 1) {
                return true;
            }
        }
        return false;
    }
};
