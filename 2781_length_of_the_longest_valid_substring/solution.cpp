// LeetCode 2781 - Length of the Longest Valid Substring
// https://leetcode.com/problems/length-of-the-longest-valid-substring/

#include <algorithm>
#include <string>
#include <unordered_set>
#include <vector>

class Solution {
public:
    int longestValidSubstring(std::string word, std::vector<std::string>& forbidden) {
        std::unordered_set<std::string> forbid;
        int maxLen = 0;
        for (auto& f : forbidden) {
            forbid.insert(f);
            maxLen = std::max(maxLen, (int)f.size());
        }
        int ans = 0, right = (int)word.size() - 1;
        for (int left = (int)word.size() - 1; left >= 0; left--) {
            for (int k = left; k <= right && k - left + 1 <= maxLen; k++) {
                if (forbid.count(word.substr(left, k - left + 1))) {
                    right = k - 1;
                    break;
                }
            }
            ans = std::max(ans, right - left + 1);
        }
        return ans;
    }
};
