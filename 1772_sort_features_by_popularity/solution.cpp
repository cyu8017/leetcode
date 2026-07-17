// LeetCode 1772 - Sort Features by Popularity
// https://leetcode.com/problems/sort-features-by-popularity/

#include <algorithm>
#include <sstream>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>

class Solution {
public:
    std::vector<std::string> sortFeatures(std::vector<std::string>& features,
                                          std::vector<std::string>& responses) {
        std::unordered_set<std::string> featureSet(features.begin(), features.end());
        std::unordered_map<std::string, int> count;
        for (const std::string& response : responses) {
            std::unordered_set<std::string> seen;
            std::istringstream stream(response);
            std::string word;
            while (stream >> word) {
                if (featureSet.count(word)) {
                    seen.insert(word);
                }
            }
            for (const std::string& word : seen) {
                count[word]++;
            }
        }
        std::vector<std::string> result = features;
        std::stable_sort(result.begin(), result.end(),
                         [&](const std::string& a, const std::string& b) {
                             int ca = count.count(a) ? count[a] : 0;
                             int cb = count.count(b) ? count[b] : 0;
                             if (ca != cb) {
                                 return ca > cb;
                             }
                             return a < b;
                         });
        return result;
    }
};
