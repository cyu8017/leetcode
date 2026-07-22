// LeetCode 1657 - Determine if Two Strings Are Close
// https://leetcode.com/problems/determine-if-two-strings-are-close/

#include <algorithm>
#include <array>
#include <string>

class Solution {
public:
    bool closeStrings(std::string word1, std::string word2) {
        if (word1.size() != word2.size()) {
            return false;
        }
        std::array<int, 26> a{};
        std::array<int, 26> b{};
        for (char c : word1) {
            ++a[c - 'a'];
        }
        for (char c : word2) {
            ++b[c - 'a'];
        }
        for (int i = 0; i < 26; ++i) {
            if ((a[i] == 0) != (b[i] == 0)) {
                return false;
            }
        }
        std::sort(a.begin(), a.end());
        std::sort(b.begin(), b.end());
        return a == b;
    }
};
