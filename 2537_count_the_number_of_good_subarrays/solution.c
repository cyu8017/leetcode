// LeetCode 2537 - Count the Number of Good Subarrays
// https://leetcode.com/problems/count-the-number-of-good-subarrays/

#include <stdlib.h>
#include <string.h>

long long countGood(int* nums, int numsSize, int k) {
    int cap = 1;
    while (cap < numsSize * 2 + 16) cap <<= 1;
    int* keys = (int*)malloc((size_t)cap * sizeof(int));
    int* vals = (int*)calloc((size_t)cap, sizeof(int));
    char* used = (char*)calloc((size_t)cap, 1);
    long long pairs = 0, ans = 0;
    int left = 0;
    for (int right = 0; right < numsSize; right++) {
        int x = nums[right];
        unsigned h = (unsigned)x * 2654435761u;
        int idx = (int)(h & (unsigned)(cap - 1));
        while (used[idx] && keys[idx] != x) idx = (idx + 1) & (cap - 1);
        pairs += vals[idx];
        keys[idx] = x; used[idx] = 1; vals[idx]++;
        while (pairs >= k) {
            ans += numsSize - right;
            int y = nums[left];
            h = (unsigned)y * 2654435761u;
            idx = (int)(h & (unsigned)(cap - 1));
            while (used[idx] && keys[idx] != y) idx = (idx + 1) & (cap - 1);
            vals[idx]--;
            pairs -= vals[idx];
            left++;
        }
    }
    free(keys); free(vals); free(used);
    return ans;
}
