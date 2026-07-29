// LeetCode 1930 - Unique Length-3 Palindromic Subsequences
// https://leetcode.com/problems/unique-length-3-palindromic-subsequences/

#include <string>
#include <unordered_set>
#include <vector>

class Solution {
public:
    int countPalindromicSubsequence(std::string s) {
        std::vector<int> first(26, -1), last(26, -1);
        for (int i = 0; i < (int)s.size(); i++) {
            int c = s[i] - 'a';
            if (first[c] == -1) first[c] = i;
            last[c] = i;
        }
        int ans = 0;
        for (int c = 0; c < 26; c++) {
            if (first[c] != -1 && last[c] - first[c] > 1) {
                std::unordered_set<char> mid;
                for (int i = first[c] + 1; i < last[c]; i++) mid.insert(s[i]);
                ans += (int)mid.size();
            }
        }
        return ans;
    }
};
