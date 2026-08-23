// LeetCode 3756 - Concatenate Non Zero Digits And Multiply By Sum Ii
// https://leetcode.com/problems/concatenate-non-zero-digits-and-multiply-by-sum-ii/

#include <string>
#include <vector>

class Solution {
    static constexpr int MX = 100001;
    static constexpr long long MOD = 1000000007;
    static const std::vector<long long>& pow10() {
        static std::vector<long long> p = [] {
            std::vector<long long> p(MX);
            p[0] = 1;
            for (int i = 1; i < MX; i++) p[i] = p[i - 1] * 10 % MOD;
            return p;
        }();
        return p;
    }

public:
    std::vector<int> sumAndMultiply(std::string s, std::vector<std::vector<int>>& queries) {
        int n = (int)s.size();
        std::vector<int> sumD(n + 1), cntN0(n + 1);
        std::vector<long long> p(n + 1);
        for (int i = 1; i <= n; i++) {
            long long d = s[i - 1] - '0';
            sumD[i] = sumD[i - 1] + (int)d;
            cntN0[i] = cntN0[i - 1];
            if (d > 0) {
                cntN0[i]++;
                p[i] = (p[i - 1] * 10 + d) % MOD;
            } else p[i] = p[i - 1];
        }
        const auto& pw = pow10();
        std::vector<int> ans(queries.size());
        for (int i = 0; i < (int)queries.size(); i++) {
            int l = queries[i][0], r = queries[i][1];
            int n0 = cntN0[r + 1] - cntN0[l];
            long long sd = sumD[r + 1] - sumD[l];
            long long x = (p[r + 1] - p[l] * pw[n0] % MOD + MOD) % MOD;
            ans[i] = (int)(x * sd % MOD);
        }
        return ans;
    }
};
