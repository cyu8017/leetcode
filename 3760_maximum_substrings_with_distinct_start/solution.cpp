// LeetCode 3760 - Maximum Substrings With Distinct Start
// https://leetcode.com/problems/maximum-substrings-with-distinct-start/

#include <string>

class Solution {
public:
    int maxDistinct(std::string s) {
        int cnt[26] = {}, ans = 0;
        for (char c : s) {
            cnt[c - 'a']++;
            if (cnt[c - 'a'] == 1) ans++;
        }
        return ans;
    }
};
