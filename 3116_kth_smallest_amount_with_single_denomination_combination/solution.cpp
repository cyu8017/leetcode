// LeetCode 3116 - Kth Smallest Amount With Single Denomination Combination
// https://leetcode.com/problems/kth-smallest-amount-with-single-denomination-combination/

#include <vector>

class Solution {
    long long gcdll(long long a, long long b) {
        while (b) { long long t = a % b; a = b; b = t; }
        return a;
    }
    long long lcmll(long long a, long long b) {
        return a / gcdll(a, b) * b;
    }
public:
    long long findKthSmallest(std::vector<int>& coins, int k) {
        long long r = 100000000000LL;
        int n = (int)coins.size();
        auto check = [&](long long mx) -> bool {
            long long cnt = 0;
            for (int i = 1; i < (1 << n); i++) {
                long long v = 1;
                for (int j = 0; j < n; j++) {
                    if ((i >> j) & 1) {
                        v = lcmll(v, coins[j]);
                        if (v > mx) break;
                    }
                }
                int m = __builtin_popcount((unsigned)i);
                if (m % 2 == 1) cnt += mx / v;
                else cnt -= mx / v;
            }
            return cnt >= k;
        };
        long long lo = 1, hi = r;
        while (lo < hi) {
            long long mid = lo + (hi - lo) / 2;
            if (check(mid)) hi = mid;
            else lo = mid + 1;
        }
        return lo;
    }
};
