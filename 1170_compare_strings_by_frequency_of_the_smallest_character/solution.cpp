// LeetCode 1170 - Compare Strings by Frequency of the Smallest Character
// https://leetcode.com/problems/compare-strings-by-frequency-of-the-smallest-character/

#include <algorithm>
#include <string>
#include <vector>

class Solution {
public:
    std::vector<int> numSmallerByFrequency(std::vector<std::string>& queries, std::vector<std::string>& words) {
        auto f = [](const std::string& s) {
            char mn = *std::min_element(s.begin(), s.end());
            return static_cast<int>(std::count(s.begin(), s.end(), mn));
        };
        std::vector<int> freqs;
        for (const auto& w : words) freqs.push_back(f(w));
        std::sort(freqs.begin(), freqs.end());
        std::vector<int> ans;
        for (const auto& q : queries) {
            int fq = f(q);
            auto it = std::upper_bound(freqs.begin(), freqs.end(), fq);
            ans.push_back(static_cast<int>(freqs.end() - it));
        }
        return ans;
    }
};
