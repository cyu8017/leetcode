// LeetCode 3662 - Filter Characters by Frequency
// https://leetcode.com/problems/filter-characters-by-frequency/

#include <string>

class Solution {
public:
    std::string filterCharacters(std::string s, int k) {
        int cnt[26] = {};
        for (char c : s) cnt[c - 'a']++;
        std::string ans;
        for (char c : s)
            if (cnt[c - 'a'] < k) ans += c;
        return ans;
    }
};
