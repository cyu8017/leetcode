// LeetCode 0737 - Sentence Similarity II
// https://leetcode.com/problems/sentence-similarity-ii/

#include <string>
#include <unordered_map>
#include <vector>

class Solution {
public:
    bool areSentencesSimilarTwo(std::vector<std::string>& sentence1, std::vector<std::string>& sentence2,
                                std::vector<std::vector<std::string>>& similarPairs) {
        if (sentence1.size() != sentence2.size()) {
            return false;
        }
        for (const auto& pair : similarPairs) {
            unite(pair[0], pair[1]);
        }
        for (size_t i = 0; i < sentence1.size(); ++i) {
            if (find(sentence1[i]) != find(sentence2[i])) {
                return false;
            }
        }
        return true;
    }

private:
    std::unordered_map<std::string, std::string> parent_;

    std::string find(const std::string& x) {
        if (!parent_.count(x)) {
            parent_[x] = x;
        }
        std::string cur = x;
        while (parent_[cur] != cur) {
            parent_[cur] = parent_[parent_[cur]];
            cur = parent_[cur];
        }
        return cur;
    }

    void unite(const std::string& a, const std::string& b) {
        parent_[find(a)] = find(b);
    }
};
