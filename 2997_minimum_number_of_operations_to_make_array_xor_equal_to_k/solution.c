// LeetCode 2997 - Minimum Number of Operations to Make Array XOR Equal to K
// https://leetcode.com/problems/minimum-number-of-operations-to-make-array-xor-equal-to-k/

int minOperations(int* nums, int numsSize, int k) {
    int xorr = 0;
    for (int i = 0; i < numsSize; i++) xorr ^= nums[i];
    int diff = xorr ^ k;
    int ans = 0;
    while (diff > 0) {
        ans += diff & 1;
        diff >>= 1;
    }
    return ans;
}
