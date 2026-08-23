// LeetCode 0340 - Longest Substring with At Most K Distinct Characters
// https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/

#include <string>
#include <unordered_map>
#include <algorithm>

class Solution {
public:
    int lengthOfLongestSubstringKDistinct(const std::string& s, int k) {
        if (k == 0) {
            return 0;
        }

        std::unordered_map<char, int> counts;
        int left = 0;
        int best = 0;

        for (int right = 0; right < static_cast<int>(s.size()); right++) {
            counts[s[right]] += 1;
            while (static_cast<int>(counts.size()) > k) {
                counts[s[left]] -= 1;
                if (counts[s[left]] == 0) {
                    counts.erase(s[left]);
                }
                left += 1;
            }
            best = std::max(best, right - left + 1);
        }

        return best;
    }
};
