// LeetCode 0003 - Longest Substring Without Repeating Characters
// https://leetcode.com/problems/longest-substring-without-repeating-characters/

#include <algorithm>
#include <string>
#include <unordered_map>

class Solution {
public:
    int lengthOfLongestSubstring(std::string s) {
        std::unordered_map<char, int> last;
        int best = 0;
        int start = 0;

        for (int i = 0; i < static_cast<int>(s.size()); i++) {
            char ch = s[i];
            auto it = last.find(ch);
            if (it != last.end() && it->second >= start) {
                start = it->second + 1;
            }
            last[ch] = i;
            best = std::max(best, i - start + 1);
        }

        return best;
    }
};
