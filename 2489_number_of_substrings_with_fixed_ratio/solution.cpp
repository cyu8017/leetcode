// LeetCode 2489 - Number of Substrings With Fixed Ratio
// https://leetcode.com/problems/number-of-substrings-with-fixed-ratio/

#include <string>
#include <unordered_map>

class Solution {
public:
    long long fixedRatio(std::string s, int num1, int num2) {
        std::unordered_map<long long, int> pref;
        pref[0] = 1;
        int zeros = 0, ones = 0;
        long long ans = 0;
        for (char c : s) {
            if (c == '0') zeros++;
            else ones++;
            long long key = 1LL * zeros * num2 - 1LL * ones * num1;
            ans += pref[key];
            pref[key]++;
        }
        return ans;
    }
};
