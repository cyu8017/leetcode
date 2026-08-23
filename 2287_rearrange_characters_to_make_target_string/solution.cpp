// LeetCode 2287 - Rearrange Characters to Make Target String
// https://leetcode.com/problems/rearrange-characters-to-make-target-string/

#include <string>
#include <array>
#include <algorithm>
#include <climits>

class Solution {
public:
    int rearrangeCharacters(std::string s, std::string target) {
        std::array<int, 26> sc{}, tc{};
        for (char c : s) sc[c - 'a']++;
        for (char c : target) tc[c - 'a']++;
        int ans = INT_MAX;
        for (int i = 0; i < 26; ++i) {
            if (tc[i] == 0) continue;
            ans = std::min(ans, sc[i] / tc[i]);
        }
        return ans;
    }
};
