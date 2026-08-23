// LeetCode 0424 - Longest Repeating Character Replacement
// https://leetcode.com/problems/longest-repeating-character-replacement/

#include <algorithm>
#include <string>
#include <unordered_map>

class Solution {
public:
    int characterReplacement(std::string s, int k) {
        std::unordered_map<char, int> counts;
        int left = 0;
        int best = 0;
        int maxCount = 0;

        for (int right = 0; right < static_cast<int>(s.size()); ++right) {
            ++counts[s[right]];
            maxCount = std::max(maxCount, counts[s[right]]);
            while ((right - left + 1) - maxCount > k) {
                --counts[s[left]];
                ++left;
            }
            best = std::max(best, right - left + 1);
        }

        return best;
    }
};
