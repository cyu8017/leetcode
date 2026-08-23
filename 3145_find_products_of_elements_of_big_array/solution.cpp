// LeetCode 3145 - Find Products of Elements of Big Array
// https://leetcode.com/problems/find-products-of-elements-of-big-array/

#include <vector>
#include <cstdint>

class Solution {
    static constexpr int M = 50;
    long long cnt[M + 1]{}, s[M + 1]{};
    void initTables() {
        long long p = 1;
        cnt[0] = 0;
        s[0] = 0;
        for (int i = 1; i <= M; i++) {
            cnt[i] = cnt[i - 1] * 2 + p;
            s[i] = s[i - 1] * 2 + p * (i - 1);
            p *= 2;
        }
    }
    std::pair<long long, long long> numIdxAndSum(long long x) {
        long long idx = 0, totalSum = 0;
        while (x > 0) {
            int i = 63 - __builtin_clzll((unsigned long long)x);
            idx += cnt[i];
            totalSum += s[i];
            x -= 1LL << i;
            totalSum += (x + 1) * i;
            idx += x + 1;
        }
        return {idx, totalSum};
    }
    long long f(long long i) {
        long long l = 0, r = 1LL << M;
        while (l < r) {
            long long mid = (l + r + 1) >> 1;
            auto [idx, _] = numIdxAndSum(mid);
            if (idx < i) l = mid;
            else r = mid - 1;
        }
        auto [_, totalSum] = numIdxAndSum(l);
        auto [idx, __] = numIdxAndSum(l);
        i -= idx;
        long long x = l + 1;
        for (long long j = 0; j < i; j++) {
            long long y = x & -x;
            totalSum += __builtin_ctzll((unsigned long long)y);
            x -= y;
        }
        return totalSum;
    }
    long long qpow(long long a, long long n, long long mod) {
        long long ans = 1 % mod;
        a %= mod;
        while (n > 0) {
            if (n & 1) ans = ans * a % mod;
            a = a * a % mod;
            n >>= 1;
        }
        return ans;
    }
public:
    Solution() { initTables(); }
    std::vector<int> findProductsOfElements(std::vector<std::vector<long long>>& queries) {
        std::vector<int> ans(queries.size());
        for (int i = 0; i < (int)queries.size(); i++) {
            long long left = queries[i][0], right = queries[i][1], mod = queries[i][2];
            long long power = f(right + 1) - f(left);
            ans[i] = (int)qpow(2, power, mod);
        }
        return ans;
    }
};
