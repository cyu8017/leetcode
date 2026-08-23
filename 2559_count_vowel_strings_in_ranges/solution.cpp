// LeetCode 2559 - Count Vowel Strings in Ranges
// https://leetcode.com/problems/count-vowel-strings-in-ranges/

#include <string>
#include <vector>

class Solution {
public:
    std::vector<int> vowelStrings(std::vector<std::string>& words, std::vector<std::vector<int>>& queries) {
        auto isV = [](char c) {
            return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
        };
        int n = (int)words.size();
        std::vector<int> pref(n + 1);
        for (int i = 0; i < n; ++i) {
            pref[i + 1] = pref[i];
            const auto& w = words[i];
            if (!w.empty() && isV(w.front()) && isV(w.back())) pref[i + 1]++;
        }
        std::vector<int> ans(queries.size());
        for (size_t i = 0; i < queries.size(); ++i) {
            ans[i] = pref[queries[i][1] + 1] - pref[queries[i][0]];
        }
        return ans;
    }
};
