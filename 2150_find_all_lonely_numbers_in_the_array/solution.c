// LeetCode 2150 - Find All Lonely Numbers in the Array
// https://leetcode.com/problems/find-all-lonely-numbers-in-the-array/

#include <stdlib.h>

int* findLonely(int* nums, int numsSize, int* returnSize) {
    int maxv = 0;
    for (int i = 0; i < numsSize; i++) if (nums[i] > maxv) maxv = nums[i];
    int* freq = (int*)calloc((size_t)maxv + 3, sizeof(int));
    for (int i = 0; i < numsSize; i++) freq[nums[i]]++;
    int* ans = (int*)malloc((size_t)numsSize * sizeof(int));
    int an = 0;
    for (int x = 0; x <= maxv; x++) {
        if (freq[x] == 1 && (x == 0 || freq[x - 1] == 0) && freq[x + 1] == 0)
            ans[an++] = x;
    }
    free(freq);
    *returnSize = an;
    return ans;
}
