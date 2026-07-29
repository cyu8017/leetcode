// LeetCode 0692 - Top K Frequent Words
// https://leetcode.com/problems/top-k-frequent-words/

#include <algorithm>
#include <string>
#include <unordered_map>
#include <vector>

class Solution {
public:
    std::vector<std::string> topKFrequent(std::vector<std::string>& words, int k) {
        std::unordered_map<std::string, int> counts;
        for (const std::string& word : words) {
            ++counts[word];
        }
        std::vector<std::string> ordered;
        for (const auto& [word, _] : counts) {
            ordered.push_back(word);
        }
        std::sort(ordered.begin(), ordered.end(), [&](const std::string& a, const std::string& b) {
            if (counts[a] != counts[b]) {
                return counts[a] > counts[b];
            }
            return a < b;
        });
        ordered.resize(k);
        return ordered;
    }
};
