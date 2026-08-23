// LeetCode 3179 - Find the N-th Value After K Seconds
// https://leetcode.com/problems/find-the-n-th-value-after-k-seconds/

#include <vector>

class Solution {
public:
    int valueAfterKSeconds(int n, int k) {
        const int mod = 1e9 + 7;
        std::vector<int> a(n, 1);
        while (k--) {
            for (int i = 1; i < n; i++) a[i] = (a[i] + a[i - 1]) % mod;
        }
        return a[n - 1];
    }
};
