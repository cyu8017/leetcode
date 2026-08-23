// LeetCode 0792 - Number of Matching Subsequences
// https://leetcode.com/problems/number-of-matching-subsequences/

#include <string>
#include <vector>

class Solution {
public:
    int numMatchingSubseq(std::string s, std::vector<std::string>& words) {
        std::vector<std::vector<std::pair<int, int>>> waiting(128);
        for (int i = 0; i < static_cast<int>(words.size()); ++i) {
            waiting[words[i][0]].push_back({i, 0});
        }
        int count = 0;
        for (char ch : s) {
            auto advance = waiting[ch];
            waiting[ch].clear();
            for (auto [wi, idx] : advance) {
                ++idx;
                if (idx == static_cast<int>(words[wi].size())) {
                    ++count;
                } else {
                    waiting[words[wi][idx]].push_back({wi, idx});
                }
            }
        }
        return count;
    }
};
