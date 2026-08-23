// LeetCode 3883 - Count Non Decreasing Arrays With Given Digit Sums
// https://leetcode.com/problems/count-non-decreasing-arrays-with-given-digit-sums/

#include <vector>

class Solution {
public:
    int countNonDecreasingArrays(std::vector<int>& digitSum) {
        const int mod = 1000000007;
        std::vector<std::vector<int>> groups(51);
        for (int x = 0; x <= 5000; x++) {
            int s = 0;
            for (int y = x; y > 0; y /= 10) s += y % 10;
            groups[s].push_back(x);
        }
        std::vector<int> prevVals = groups[digitSum[0]];
        std::vector<int> dp(prevVals.size(), 1);
        for (int pos = 1; pos < (int)digitSum.size(); pos++) {
            std::vector<int>& curVals = groups[digitSum[pos]];
            std::vector<int> next(curVals.size(), 0);
            int j = 0, prefix = 0;
            for (int i = 0; i < (int)curVals.size(); i++) {
                int x = curVals[i];
                while (j < (int)prevVals.size() && prevVals[j] <= x) {
                    prefix += dp[j];
                    if (prefix >= mod) prefix -= mod;
                    j++;
                }
                next[i] = prefix;
            }
            prevVals = curVals;
            dp = next;
        }
        int ans = 0;
        for (int x : dp) {
            ans += x;
            if (ans >= mod) ans -= mod;
        }
        return ans;
    }
};
