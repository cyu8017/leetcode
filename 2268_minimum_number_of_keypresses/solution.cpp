// LeetCode 2268 - Minimum Number of Keypresses
// https://leetcode.com/problems/minimum-number-of-keypresses/

#include <string>
#include <vector>
#include <algorithm>

class Solution {
public:
    int minimumKeypresses(std::string s) {
        std::vector<int> freq(26);
        for (char c : s) freq[c - 'a']++;
        std::sort(freq.rbegin(), freq.rend());
        int ans = 0;
        for (int i = 0; i < 26; ++i) {
            if (freq[i] == 0) break;
            ans += freq[i] * (i / 9 + 1);
        }
        return ans;
    }
};
