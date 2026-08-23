// LeetCode 3913 - Sort Vowels By Frequency
// https://leetcode.com/problems/sort-vowels-by-frequency/

#include <algorithm>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>

class Solution {
public:
    std::string sortVowels(std::string s) {
        std::unordered_set<char> st = {'a', 'e', 'i', 'o', 'u'};
        std::vector<char> vowels;
        std::unordered_map<char, int> cnt;
        for (char c : s) {
            if (!st.count(c)) continue;
            if (!cnt.count(c)) vowels.push_back(c);
            cnt[c]++;
        }
        std::sort(vowels.begin(), vowels.end(), [&](char a, char b) {
            return cnt[a] > cnt[b];
        });
        std::string ans = s;
        int i = 0;
        for (int k = 0; k < (int)s.size(); k++) {
            if (!st.count(s[k])) continue;
            char ch = vowels[i];
            ans[k] = ch;
            if (--cnt[ch] == 0) i++;
        }
        return ans;
    }
};
