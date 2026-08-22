// LeetCode 3712 - Sum of Elements With Frequency Divisible by K
// https://leetcode.com/problems/sum-of-elements-with-frequency-divisible-by-k/

#include <string.h>

#define MAP_SIZE 200003
static int mk[MAP_SIZE], mv[MAP_SIZE];
static char mu[MAP_SIZE];

int sumDivisibleByK(int* nums, int numsSize, int k) {
    memset(mu, 0, sizeof(mu));
    for (int i = 0; i < numsSize; i++) {
        int key = nums[i];
        int idx = (int)((unsigned)key % MAP_SIZE);
        while (mu[idx] && mk[idx] != key) { if (++idx == MAP_SIZE) idx = 0; }
        if (!mu[idx]) { mu[idx] = 1; mk[idx] = key; mv[idx] = 0; }
        mv[idx]++;
    }
    int ans = 0;
    for (int i = 0; i < MAP_SIZE; i++) {
        if (mu[i] && mv[i] % k == 0) ans += mk[i] * mv[i];
    }
    return ans;
}
