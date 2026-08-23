// LeetCode 3016 - Minimum Number of Pushes to Type Word II
// https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii/

#include <algorithm>
#include <string>
#include <vector>

class Solution {
public:
    int minimumPushes(std::string word) {
        std::vector<int> cnt(26, 0);
        for (char c : word) cnt[c - 'a']++;
        std::sort(cnt.begin(), cnt.end());
        int ans = 0;
        for (int i = 0; i < 26; i++) ans += (i / 8 + 1) * cnt[26 - i - 1];
        return ans;
    }
};
