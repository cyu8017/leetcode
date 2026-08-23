// LeetCode 2743 - Count Substrings Without Repeating Character
// https://leetcode.com/problems/count-substrings-without-repeating-character/

#include <string>

class Solution {
public:
    int numberOfSpecialSubstrings(std::string s) {
        int n = (int)s.size(), ans = 0, left = 0;
        int cnt[26] = {};
        for (int i = 0; i < n; i++) {
            int c = s[i] - 'a';
            cnt[c]++;
            while (cnt[c] > 1) { cnt[s[left] - 'a']--; left++; }
            ans += i - left + 1;
        }
        return ans;
    }
};
