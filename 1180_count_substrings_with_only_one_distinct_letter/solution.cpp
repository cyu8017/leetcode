// LeetCode 1180 - Count Substrings with Only One Distinct Letter
// https://leetcode.com/problems/count-substrings-with-only-one-distinct-letter/

#include <string>

class Solution {
public:
    int countLetters(std::string s) {
        int ans = 1, length = 1;
        for (int i = 1; i < static_cast<int>(s.size()); ++i) {
            length = s[i] == s[i - 1] ? length + 1 : 1;
            ans += length;
        }
        return ans;
    }
};
