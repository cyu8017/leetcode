// LeetCode 2516 - Take K of Each Character From Left and Right
// https://leetcode.com/problems/take-k-of-each-character-from-left-and-right/

#include <string>

class Solution {
public:
    int takeCharacters(std::string s, int k) {
        int n = (int)s.size();
        int cnt[3] = {};
        for (char c : s) cnt[c - 'a']++;
        if (cnt[0] < k || cnt[1] < k || cnt[2] < k) return -1;
        int need[3] = {cnt[0] - k, cnt[1] - k, cnt[2] - k};
        int window[3] = {};
        int left = 0, maxMid = 0;
        for (int right = 0; right < n; right++) {
            window[s[right] - 'a']++;
            while (window[0] > need[0] || window[1] > need[1] || window[2] > need[2]) {
                window[s[left] - 'a']--;
                left++;
            }
            if (right - left + 1 > maxMid) maxMid = right - left + 1;
        }
        return n - maxMid;
    }
};
