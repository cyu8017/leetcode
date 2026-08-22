// LeetCode 3792 - Sum Of Increasing Product Blocks
// https://leetcode.com/problems/sum-of-increasing-product-blocks/

int sumOfBlocks(int n) {
    const int mod = 1000000007;
    int ans = 0;
    int k = 1;
    for (int i = 1; i <= n; i++) {
        long long x = 1;
        for (int j = k; j < k + i; j++) x = x * j % mod;
        ans = (int)((ans + x) % mod);
        k += i;
    }
    return ans;
}
