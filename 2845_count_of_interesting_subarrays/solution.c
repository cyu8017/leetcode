// LeetCode 2845 - Count of Interesting Subarrays
// https://leetcode.com/problems/count-of-interesting-subarrays/

#include <stdlib.h>

long long countInterestingSubarrays(int* nums, int numsSize, int modulo, int k) {
    int* freq = (int*)calloc(modulo, sizeof(int));
    freq[0] = 1;
    long long ans = 0;
    int pref = 0;
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] % modulo == k) pref++;
        int need = (pref - k) % modulo;
        if (need < 0) need += modulo;
        ans += freq[need];
        freq[pref % modulo]++;
    }
    free(freq);
    return ans;
}
