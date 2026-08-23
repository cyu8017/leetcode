// LeetCode 3889 - Mirror Frequency Distance
// https://leetcode.com/problems/mirror-frequency-distance/

#include <cmath>
#include <string>
#include <unordered_map>

class Solution {
public:
    int mirrorFrequency(std::string s) {
        std::unordered_map<char, int> freq;
        for (char c : s) freq[c]++;
        int ans = 0;
        std::unordered_map<char, bool> vis;
        for (auto& [c, v] : freq) {
            char m;
            if (c >= 'a' && c <= 'z') m = (char)('a' + 25 - (c - 'a'));
            else m = (char)('0' + (9 - (c - '0')));
            if (vis[m]) continue;
            vis[c] = true;
            int mv = freq.count(m) ? freq[m] : 0;
            ans += std::abs(v - mv);
        }
        return ans;
    }
};
