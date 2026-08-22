// LeetCode 3632 - Subarrays With XOR At Least K
// https://leetcode.com/problems/subarrays-with-xor-at-least-k/

long long subarraysWithXorAtLeastK(int* nums, int numsSize, int k) {
    long long ans = 0;
    for (int i = 0; i < numsSize; i++) {
        int x = 0;
        for (int j = i; j < numsSize; j++) { x ^= nums[j]; if (x >= k) ans++; }
    }
    return ans;
}
