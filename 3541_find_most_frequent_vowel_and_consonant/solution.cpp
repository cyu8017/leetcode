// LeetCode 3541 - Find Most Frequent Vowel and Consonant
// https://leetcode.com/problems/find-most-frequent-vowel-and-consonant/

#include <string>
#include <algorithm>

class Solution {
public:
    int maxFreqSum(std::string s) {
        int cnt[26] = {};
        for (char c : s) cnt[c - 'a']++;
        int a = 0, b = 0;
        for (int i = 0; i < 26; i++) {
            char c = char(i + 'a');
            if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u')
                a = std::max(a, cnt[i]);
            else b = std::max(b, cnt[i]);
        }
        return a + b;
    }
};
