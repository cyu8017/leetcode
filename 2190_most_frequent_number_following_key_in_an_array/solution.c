// LeetCode 2190 - Most Frequent Number Following Key In an Array
// https://leetcode.com/problems/most-frequent-number-following-key-in-an-array/

#include <stdlib.h>

int mostFrequent(int* nums, int numsSize, int key) {
    int maxv = 0;
    for (int i = 0; i < numsSize; i++) if (nums[i] > maxv) maxv = nums[i];
    int* freq = (int*)calloc((size_t)maxv + 1, sizeof(int));
    int best = 0, ans = 0;
    for (int i = 0; i + 1 < numsSize; i++) {
        if (nums[i] == key) {
            freq[nums[i + 1]]++;
            if (freq[nums[i + 1]] > best) { best = freq[nums[i + 1]]; ans = nums[i + 1]; }
        }
    }
    free(freq);
    return ans;
}
