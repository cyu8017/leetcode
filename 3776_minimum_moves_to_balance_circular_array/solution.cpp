// LeetCode 3776 - Minimum Moves To Balance Circular Array
// https://leetcode.com/problems/minimum-moves-to-balance-circular-array/

#include <algorithm>
#include <cstdint>
#include <vector>

class Solution {
public:
    long long minMoves(std::vector<int>& balance) {
        int64_t sum = 0;
        for (int b : balance) sum += b;
        if (sum < 0) return -1;

        int n = (int)balance.size();
        int mn = balance[0], idx = 0;
        for (int i = 1; i < n; i++) {
            if (balance[i] < mn) {
                mn = balance[i];
                idx = i;
            }
        }
        if (mn >= 0) return 0;

        int need = -mn;
        int64_t ans = 0;
        for (int j = 1; j < n; j++) {
            int a = balance[(idx - j + n) % n];
            int b = balance[(idx + j) % n];
            int c1 = std::min(a, need);
            need -= c1;
            ans += (int64_t)c1 * j;
            int c2 = std::min(b, need);
            need -= c2;
            ans += (int64_t)c2 * j;
        }
        return ans;
    }
};
