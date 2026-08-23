// LeetCode 3838 - Weighted Word Mapping
// https://leetcode.com/problems/weighted-word-mapping/

#include <string>
#include <vector>

class Solution {
public:
    std::string mapWordWeights(std::vector<std::string>& words, std::vector<int>& weights) {
        std::string ans;
        ans.reserve(words.size());
        for (auto& w : words) {
            int s = 0;
            for (char c : w) s = (s + weights[c - 'a']) % 26;
            ans.push_back(char('a' + (25 - s)));
        }
        return ans;
    }
};
