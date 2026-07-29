// LeetCode 1513 - Number of Substrings With Only 1s
// https://leetcode.com/problems/number-of-substrings-with-only-1s/

#include <string>

class Solution {
public:
    int numSub(std::string s) {
        long long ans = 0;
        long long run = 0;
        for (char ch : s) {
            run = ch == '1' ? run + 1 : 0;
            ans += run;
        }
        return static_cast<int>(ans % 1000000007);
    }
};
