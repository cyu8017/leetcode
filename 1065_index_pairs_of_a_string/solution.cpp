// LeetCode 1065 - Index Pairs of a String
// https://leetcode.com/problems/index-pairs-of-a-string/

#include <string>
#include <unordered_set>
#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> indexPairs(std::string text, std::vector<std::string>& words) {
        std::unordered_set<std::string> wordSet(words.begin(), words.end());
        std::vector<std::vector<int>> ans;
        int n = static_cast<int>(text.size());
        for (int i = 0; i < n; ++i) {
            for (int j = i; j < n; ++j) {
                if (wordSet.count(text.substr(i, j - i + 1))) {
                    ans.push_back({i, j});
                }
            }
        }
        return ans;
    }
};
