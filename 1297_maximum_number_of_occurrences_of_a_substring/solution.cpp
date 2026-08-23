// LeetCode 1297 - Maximum Number of Occurrences of a Substring
// https://leetcode.com/problems/maximum-number-of-occurrences-of-a-substring/

#include <algorithm>
#include <string>
#include <unordered_map>
#include <unordered_set>

class Solution {
public:
    int maxFreq(std::string s, int maxLetters, int minSize, int maxSize) {
        (void)maxSize;
        std::unordered_map<std::string, int> counts;
        int best = 0;
        for (int i = 0; i + minSize <= static_cast<int>(s.size()); ++i) {
            std::string sub = s.substr(i, minSize);
            std::unordered_set<char> unique(sub.begin(), sub.end());
            if (static_cast<int>(unique.size()) <= maxLetters) {
                best = std::max(best, ++counts[sub]);
            }
        }
        return best;
    }
};
