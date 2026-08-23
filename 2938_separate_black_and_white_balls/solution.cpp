// LeetCode 2938 - Separate Black and White Balls
// https://leetcode.com/problems/separate-black-and-white-balls/

#include <string>

class Solution {
public:
    long long minimumSteps(std::string s) {
        long long ans = 0, zeros = 0;
        for (int i = (int)s.size() - 1; i >= 0; i--) {
            if (s[i] == '0') zeros++;
            else ans += zeros;
        }
        return ans;
    }
};
