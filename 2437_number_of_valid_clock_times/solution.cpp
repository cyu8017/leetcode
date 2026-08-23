// LeetCode 2437 - Number of Valid Clock Times
// https://leetcode.com/problems/number-of-valid-clock-times/

#include <string>

class Solution {
public:
    int countTime(std::string time) {
        int ans = 0;
        for (int h = 0; h < 24; h++) {
            for (int m = 0; m < 60; m++) {
                char hs[2] = {char('0' + h / 10), char('0' + h % 10)};
                char ms[2] = {char('0' + m / 10), char('0' + m % 10)};
                if (time[0] != '?' && time[0] != hs[0]) continue;
                if (time[1] != '?' && time[1] != hs[1]) continue;
                if (time[3] != '?' && time[3] != ms[0]) continue;
                if (time[4] != '?' && time[4] != ms[1]) continue;
                ans++;
            }
        }
        return ans;
    }
};
