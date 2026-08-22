// LeetCode 3247 - Number of Subsequences with Odd Sum
// https://leetcode.com/problems/number-of-subsequences-with-odd-sum/

int subsequenceCount(int* nums, int numsSize) {
    const int mod = 1000000007;
    int f0 = 0, f1 = 0;
    for (int i = 0; i < numsSize; i++) {
        int g0, g1;
        if (nums[i] % 2 == 1) {
            g0 = (f0 + f1) % mod;
            g1 = (f0 + f1 + 1) % mod;
        } else {
            g0 = (f0 + f0 + 1) % mod;
            g1 = (f1 + f1) % mod;
        }
        f0 = g0; f1 = g1;
    }
    return f1;
}
