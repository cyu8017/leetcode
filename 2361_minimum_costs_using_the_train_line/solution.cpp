// LeetCode 2361 - Minimum Costs Using the Train Line
// https://leetcode.com/problems/minimum-costs-using-the-train-line/

#include <algorithm>
#include <vector>

class Solution {
public:
    std::vector<long long> minimumCosts(std::vector<int>& regular, std::vector<int>& express, int expressCost) {
        int n = (int)regular.size();
        std::vector<long long> ans(n);
        long long reg = 0, exp = expressCost;
        for (int i = 0; i < n; i++) {
            long long nextReg = std::min(reg + regular[i], exp + express[i]);
            long long nextExp = std::min(reg + regular[i] + expressCost, exp + express[i]);
            reg = nextReg;
            exp = nextExp;
            ans[i] = std::min(reg, exp);
        }
        return ans;
    }
};
