// LeetCode 0734 - Sentence Similarity
// https://leetcode.com/problems/sentence-similarity/

#include <string>
#include <unordered_set>
#include <vector>

class Solution {
public:
    bool areSentencesSimilar(std::vector<std::string>& sentence1, std::vector<std::string>& sentence2,
                             std::vector<std::vector<std::string>>& similarPairs) {
        if (sentence1.size() != sentence2.size()) {
            return false;
        }
        std::unordered_set<std::string> pairs;
        for (const auto& pair : similarPairs) {
            pairs.insert(pair[0] + "#" + pair[1]);
            pairs.insert(pair[1] + "#" + pair[0]);
        }
        for (size_t i = 0; i < sentence1.size(); ++i) {
            if (sentence1[i] != sentence2[i] &&
                !pairs.count(sentence1[i] + "#" + sentence2[i])) {
                return false;
            }
        }
        return true;
    }
};
