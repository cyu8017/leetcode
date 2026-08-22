// LeetCode 1248 - Count Number of Nice Subarrays
// https://leetcode.com/problems/count-number-of-nice-subarrays/

#include <stdlib.h>
#include <string.h>

int numberOfSubarrays(int* nums, int numsSize, int k) {
    int maxOdd = numsSize + 1;
    int* freq = (int*)calloc((size_t)maxOdd, sizeof(int));
    freq[0] = 1;
    int odd = 0, answer = 0;
    for (int i = 0; i < numsSize; i++) {
        odd += nums[i] & 1;
        if (odd - k >= 0) answer += freq[odd - k];
        freq[odd]++;
    }
    free(freq);
    return answer;
}
