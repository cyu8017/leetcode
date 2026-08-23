// LeetCode 3792 - Sum Of Increasing Product Blocks
// https://leetcode.com/problems/sum-of-increasing-product-blocks/

class Solution {
public:
    int sumOfBlocks(int n) {
        const int MOD = 1e9 + 7;
        int ans = 0, k = 1;
        for (int i = 1; i <= n; i++) {
            int x = 1;
            for (int j = k; j < k + i; j++) x = (int)((long long)x * j % MOD);
            ans = (ans + x) % MOD;
            k += i;
        }
        return ans;
    }
};
