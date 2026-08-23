// LeetCode 3335 - Total Characters in String After Transformations I
// https://leetcode.com/problems/total-characters-in-string-after-transformations-i/

#include <array>
#include <string>

class Solution {
public:
    int lengthAfterTransformations(std::string s, int t) {
        const int mod = 1000000007;
        std::array<int, 26> cnt{};
        for (char c : s) cnt[c - 'a']++;
        for (int step = 0; step < t; step++) {
            std::array<int, 26> ncnt{};
            for (int i = 0; i < 25; i++) ncnt[i + 1] = (ncnt[i + 1] + cnt[i]) % mod;
            ncnt[0] = (ncnt[0] + cnt[25]) % mod;
            ncnt[1] = (ncnt[1] + cnt[25]) % mod;
            cnt = ncnt;
        }
        int ans = 0;
        for (int v : cnt) ans = (ans + v) % mod;
        return ans;
    }
};
