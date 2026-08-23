// LeetCode 3849 - Maximum Bitwise Xor After Rearrangement
// https://leetcode.com/problems/maximum-bitwise-xor-after-rearrangement/

#include <string>

class Solution {
public:
    std::string maximumXor(std::string s, std::string t) {
        int cnt[2] = {};
        for (char c : t) cnt[c - '0']++;
        std::string ans(s.size(), '0');
        for (int i = 0; i < (int)s.size(); i++) {
            int x = s[i] - '0';
            if (cnt[x ^ 1] > 0) {
                cnt[x ^ 1]--;
                ans[i] = '1';
            } else {
                cnt[x]--;
                ans[i] = '0';
            }
        }
        return ans;
    }
};
