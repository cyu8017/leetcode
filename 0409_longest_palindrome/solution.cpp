// LeetCode 0409 - Longest Palindrome
// https://leetcode.com/problems/longest-palindrome/

#include <string>
#include <unordered_map>

class Solution {
public:
    int longestPalindrome(string s) {
        unordered_map<char, int> counts;
        for (char ch : s) {
            ++counts[ch];
        }

        int length = 0;
        bool hasOdd = false;
        for (const auto& entry : counts) {
            length += (entry.second / 2) * 2;
            if (entry.second % 2) {
                hasOdd = true;
            }
        }

        return length + (hasOdd ? 1 : 0);
    }
};
