// LeetCode 3545 - Minimum Deletions for At Most K Distinct Characters
// https://leetcode.com/problems/minimum-deletions-for-at-most-k-distinct-characters/

#include <string>
#include <vector>
#include <algorithm>

class Solution {
public:
    int minDeletion(std::string s, int k) {
        std::vector<int> cnt(26);
        for (char c : s) cnt[c - 'a']++;
        std::sort(cnt.begin(), cnt.end());
        int ans = 0;
        for (int i = 0; i + k < 26; i++) ans += cnt[i];
        return ans;
    }
};
