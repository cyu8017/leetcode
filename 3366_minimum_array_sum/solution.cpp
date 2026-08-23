// LeetCode 3366 - Minimum Array Sum
// https://leetcode.com/problems/minimum-array-sum/

#include <climits>
#include <vector>

class Solution {
public:
    int minArraySum(std::vector<int>& nums, int k, int op1, int op2) {
        const long long inf = (long long)1e18;
        std::vector<std::vector<long long>> dp(op1 + 1, std::vector<long long>(op2 + 1, inf));
        dp[0][0] = 0;
        for (int x : nums) {
            std::vector<std::vector<long long>> ndp(op1 + 1, std::vector<long long>(op2 + 1, inf));
            for (int a = 0; a <= op1; a++) {
                for (int b = 0; b <= op2; b++) {
                    if (dp[a][b] == inf) continue;
                    struct Cand { int na, nb, v; };
                    std::vector<Cand> cand{{a, b, x}};
                    if (a < op1) cand.push_back({a + 1, b, (x + 1) / 2});
                    if (b < op2 && x >= k) cand.push_back({a, b + 1, x - k});
                    if (a < op1 && b < op2) {
                        int v1 = (x + 1) / 2;
                        if (v1 >= k) cand.push_back({a + 1, b + 1, v1 - k});
                        if (x >= k) cand.push_back({a + 1, b + 1, (x - k + 1) / 2});
                    }
                    for (auto& c : cand) {
                        if (dp[a][b] + c.v < ndp[c.na][c.nb]) ndp[c.na][c.nb] = dp[a][b] + c.v;
                    }
                }
            }
            dp.swap(ndp);
        }
        long long ans = inf;
        for (int a = 0; a <= op1; a++)
            for (int b = 0; b <= op2; b++)
                if (dp[a][b] < ans) ans = dp[a][b];
        return (int)ans;
    }
};
