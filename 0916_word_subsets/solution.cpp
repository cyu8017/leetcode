// LeetCode 0916 - Word Subsets
// https://leetcode.com/problems/word-subsets/

#include <algorithm>
#include <string>
#include <vector>

class Solution {
public:
    std::vector<std::string> wordSubsets(std::vector<std::string>& words1, std::vector<std::string>& words2) {
        int need[26] = {};
        for (const auto& w : words2) {
            int cnt[26] = {};
            for (char c : w) cnt[c - 'a']++;
            for (int i = 0; i < 26; i++) need[i] = std::max(need[i], cnt[i]);
        }
        std::vector<std::string> ans;
        for (const auto& w : words1) {
            int cnt[26] = {};
            for (char c : w) cnt[c - 'a']++;
            bool ok = true;
            for (int i = 0; i < 26; i++) {
                if (cnt[i] < need[i]) { ok = false; break; }
            }
            if (ok) ans.push_back(w);
        }
        return ans;
    }
};
