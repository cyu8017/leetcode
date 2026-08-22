// LeetCode 2932 - Maximum Strong Pair XOR I
// https://leetcode.com/problems/maximum-strong-pair-xor-i/

int maximumStrongPairXor(int* nums, int numsSize) {
    int ans = 0;
    for (int i = 0; i < numsSize; i++) {
        for (int j = i; j < numsSize; j++) {
            int x = nums[i], y = nums[j];
            int d = x - y; if (d < 0) d = -d;
            int mn = x < y ? x : y;
            if (d <= mn) {
                int xorr = x ^ y;
                if (xorr > ans) ans = xorr;
            }
        }
    }
    return ans;
}
