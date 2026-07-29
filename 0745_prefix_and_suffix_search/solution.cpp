// LeetCode 0745 - Prefix and Suffix Search
// https://leetcode.com/problems/prefix-and-suffix-search/

#include <string>
#include <unordered_map>
#include <vector>

class WordFilter {
public:
    WordFilter(std::vector<std::string>& words) {
        for (int index = 0; index < static_cast<int>(words.size()); ++index) {
            const std::string& word = words[index];
            int size = static_cast<int>(word.size());
            for (int i = 0; i <= size; ++i) {
                for (int j = 0; j <= size; ++j) {
                    lookup_[word.substr(0, i) + "#" + word.substr(j)] = index;
                }
            }
        }
    }

    int f(std::string pref, std::string suff) {
        auto it = lookup_.find(pref + "#" + suff);
        return it == lookup_.end() ? -1 : it->second;
    }

private:
    std::unordered_map<std::string, int> lookup_;
};
