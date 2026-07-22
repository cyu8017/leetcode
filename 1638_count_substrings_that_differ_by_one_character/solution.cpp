// LeetCode 1638 - Count Substrings That Differ by One Character
// https://leetcode.com/problems/count-substrings-that-differ-by-one-character/

#include <algorithm>
#include <string>

class Solution {
public:
    int countSubstrings(std::string s, std::string t) {
        int ans = 0;
        for (int i = 0; i < static_cast<int>(s.size()); ++i) {
            for (int j = 0; j < static_cast<int>(t.size()); ++j) {
                int diff = 0;
                for (int k = 0; k < std::min(static_cast<int>(s.size()) - i, static_cast<int>(t.size()) - j); ++k) {
                    diff += s[i + k] != t[j + k];
                    if (diff == 1) {
                        ++ans;
                    } else if (diff > 1) {
                        break;
                    }
                }
            }
        }
        return ans;
    }
};
