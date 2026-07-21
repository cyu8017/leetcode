// LeetCode 1838 - Frequency of the Most Frequent Element
// https://leetcode.com/problems/frequency-of-the-most-frequent-element/

#include <stdlib.h>

static int cmpInt(const void* a, const void* b) {
    int x = *(const int*)a, y = *(const int*)b;
    return (x > y) - (x < y);
}

int maxFrequency(int* nums, int numsSize, int k) {
    qsort(nums, (size_t)numsSize, sizeof(int), cmpInt);
    int left = 0;
    long long windowSum = 0;
    int best = 0;
    for (int right = 0; right < numsSize; right++) {
        windowSum += nums[right];
        while ((long long)nums[right] * (right - left + 1) - windowSum > k) {
            windowSum -= nums[left];
            left++;
        }
        int len = right - left + 1;
        if (len > best) best = len;
    }
    return best;
}
