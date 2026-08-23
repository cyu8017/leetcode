// LeetCode 3389 - Minimum Operations to Make Character Frequencies Equal
// https://leetcode.com/problems/minimum-operations-to-make-character-frequencies-equal/

#include <algorithm>
#include <string>

class Solution {
public:
    int makeStringGood(std::string s) {
        int freq[26] = {};
        for (char c : s) freq[c - 'a']++;
        int ans = (int)s.size();
        for (int t = 1; t <= (int)s.size(); t++) {
            int pool = 0;
            for (int i = 0; i < 26; i++) if (freq[i] > t) pool += freq[i] - t;
            int deficit = 0;
            for (int i = 0; i < 26; i++) if (freq[i] < t) deficit += t - freq[i];
            int ops = (pool >= deficit) ? pool : deficit;
            if (ops < ans) ans = ops;
        }
        if ((int)s.size() < ans) ans = (int)s.size();
        return ans;
    }
};
