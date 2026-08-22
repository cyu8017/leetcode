// LeetCode 2964 - Number of Divisible Triplet Sums
// https://leetcode.com/problems/number-of-divisible-triplet-sums/

#include <stdlib.h>
#include <string.h>

int divisibleTripletCount(int* nums, int numsSize, int d) {
    int ans = 0;
    int* freq = (int*)malloc((size_t)d * sizeof(int));
    for (int i = 0; i < numsSize; i++) {
        memset(freq, 0, (size_t)d * sizeof(int));
        for (int j = i + 1; j < numsSize; j++) {
            int need = (d - (nums[i] + nums[j]) % d) % d;
            ans += freq[need];
            freq[nums[j] % d]++;
        }
    }
    free(freq);
    return ans;
}
