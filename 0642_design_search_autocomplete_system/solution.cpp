// LeetCode 0642 - Design Search Autocomplete System
// https://leetcode.com/problems/design-search-autocomplete-system/

#include <algorithm>
#include <string>
#include <unordered_map>
#include <vector>

class AutocompleteSystem {
    std::unordered_map<std::string, int> counts_;
    std::string current_;

public:
    AutocompleteSystem(std::vector<std::string>& sentences, std::vector<int>& times) {
        for (std::size_t i = 0; i < sentences.size(); ++i) {
            counts_[sentences[i]] += times[i];
        }
    }

    std::vector<std::string> input(char c) {
        if (c == '#') {
            ++counts_[current_];
            current_.clear();
            return {};
        }
        current_ += c;
        std::vector<std::string> matches;
        for (const auto& [sentence, _] : counts_) {
            if (sentence.compare(0, current_.size(), current_) == 0) {
                matches.push_back(sentence);
            }
        }
        std::sort(matches.begin(), matches.end(), [&](const std::string& a, const std::string& b) {
            if (counts_[a] != counts_[b]) {
                return counts_[a] > counts_[b];
            }
            return a < b;
        });
        if (matches.size() > 3) {
            matches.resize(3);
        }
        return matches;
    }
};
