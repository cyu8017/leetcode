// LeetCode 3146 - Permutation Difference between Two Strings
// https://leetcode.com/problems/permutation-difference-between-two-strings/

#include <string>
#include <array>
#include <cstdlib>

class Solution {
public:
    int findPermutationDifference(std::string s, std::string t) {
        std::array<int, 26> d{};
        for (int i = 0; i < (int)s.size(); i++) d[s[i] - 'a'] = i;
        int ans = 0;
        for (int i = 0; i < (int)t.size(); i++) ans += std::abs(d[t[i] - 'a'] - i);
        return ans;
    }
};
