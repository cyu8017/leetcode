// LeetCode 1181 - Before and After Puzzle
// https://leetcode.com/problems/before-and-after-puzzle/

#include <algorithm>
#include <set>
#include <sstream>
#include <string>
#include <vector>

class Solution {
public:
    std::vector<std::string> beforeAndAfterPuzzles(std::vector<std::string>& phrases) {
        std::vector<std::vector<std::string>> split;
        for (const auto& p : phrases) {
            std::stringstream ss(p);
            std::vector<std::string> words;
            std::string w;
            while (ss >> w) words.push_back(w);
            split.push_back(std::move(words));
        }
        std::set<std::string> result;
        int n = static_cast<int>(split.size());
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                if (i == j) continue;
                if (split[i].back() == split[j].front()) {
                    std::string merged = split[i][0];
                    for (size_t k = 1; k < split[i].size(); ++k) merged += " " + split[i][k];
                    for (size_t k = 1; k < split[j].size(); ++k) merged += " " + split[j][k];
                    result.insert(merged);
                }
            }
        }
        return std::vector<std::string>(result.begin(), result.end());
    }
};
