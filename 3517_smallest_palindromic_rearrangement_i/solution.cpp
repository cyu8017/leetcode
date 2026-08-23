// LeetCode 3517 - Smallest Palindromic Rearrangement I
// https://leetcode.com/problems/smallest-palindromic-rearrangement-i/

#include <string>
#include <vector>

class Solution {
public:
    std::string smallestPalindrome(std::string s) {
        std::vector<int> cnt(26);
        for (char c : s) cnt[c - 'a']++;
        std::string t;
        char ch = 0;
        for (char c = 'a'; c <= 'z'; c++) {
            int v = cnt[c - 'a'] / 2;
            t.append(v, c);
            cnt[c - 'a'] -= v * 2;
            if (cnt[c - 'a'] == 1) ch = c;
        }
        std::string sb = t;
        if (ch) sb.push_back(ch);
        for (int i = (int)t.size() - 1; i >= 0; i--) sb.push_back(t[i]);
        return sb;
    }
};
