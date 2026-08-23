// LeetCode 3821 - Find Nth Smallest Integer With K One Bits
// https://leetcode.com/problems/find-nth-smallest-integer-with-k-one-bits/

#include <cstdint>

class Solution {
    static constexpr int MX = 50;
    static int64_t C[MX][MX + 1];
    static bool inited;

    static void init() {
        if (inited) return;
        for (int i = 0; i < MX; i++) {
            C[i][0] = 1;
            for (int j = 1; j <= i; j++) C[i][j] = C[i - 1][j - 1] + C[i - 1][j];
        }
        inited = true;
    }

public:
    long long nthSmallest(long long n, int k) {
        init();
        int64_t ans = 0;
        for (int i = 49; i >= 0; i--) {
            if (n > C[i][k]) {
                n -= C[i][k];
                ans |= 1LL << i;
                k--;
                if (k == 0) break;
            }
        }
        return ans;
    }
};

int64_t Solution::C[Solution::MX][Solution::MX + 1];
bool Solution::inited = false;
