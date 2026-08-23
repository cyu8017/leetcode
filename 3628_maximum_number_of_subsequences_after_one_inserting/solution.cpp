// LeetCode 3628 - Maximum Number of Subsequences After One Inserting
// https://leetcode.com/problems/maximum-number-of-subsequences-after-one-inserting/

#include <algorithm>
#include <string>

class Solution {
public:
    long long numOfSubsequences(std::string s) {
        auto calc = [&](const std::string& t) {
            long long cnt = 0, a = 0;
            for (char c : s) {
                if (c == t[1]) cnt += a;
                if (c == t[0]) a++;
            }
            return cnt;
        };
        long long l = 0, r = 0;
        for (char c : s)
            if (c == 'T') r++;
        long long ans = 0, mx = 0;
        for (char c : s) {
            if (c == 'T') r--;
            if (c == 'C') ans += l * r;
            if (c == 'L') l++;
            mx = std::max(mx, l * r);
        }
        mx = std::max({mx, calc("LC"), calc("CT")});
        return ans + mx;
    }
};
