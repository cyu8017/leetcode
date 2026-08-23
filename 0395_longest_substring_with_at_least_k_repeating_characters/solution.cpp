// LeetCode 0395 - Longest Substring with At Least K Repeating Characters
// https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/

#include <algorithm>
#include <string>
#include <unordered_map>

class Solution {
public:
    int longestSubstring(std::string s, int k) {
        if (s.empty()) {
            return 0;
        }

        std::unordered_map<char, int> counts;
        for (char ch : s) {
            counts[ch] += 1;
        }

        for (const auto& entry : counts) {
            if (entry.second < k) {
                int best = 0;
                std::string part;
                for (char ch : s) {
                    if (ch == entry.first) {
                        best = std::max(best, longestSubstring(part, k));
                        part.clear();
                    } else {
                        part += ch;
                    }
                }
                best = std::max(best, longestSubstring(part, k));
                return best;
            }
        }

        return static_cast<int>(s.size());
    }
};
