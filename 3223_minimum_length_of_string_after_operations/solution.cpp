// LeetCode 3223 - Minimum Length of String After Operations
// https://leetcode.com/problems/minimum-length-of-string-after-operations/

#include <string>
#include <array>

class Solution {
public:
    int minimumLength(std::string s) {
        std::array<int, 26> cnt{};
        for (char c : s) cnt[c - 'a']++;
        int ans = 0;
        for (int x : cnt) {
            if (x > 0) ans += (x & 1) ? 1 : 2;
        }
        return ans;
    }
};
