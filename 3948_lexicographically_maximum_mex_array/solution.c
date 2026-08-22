// LeetCode 3948 - Lexicographically Maximum MEX Array
// https://leetcode.com/problems/lexicographically-maximum-mex-array/

#include <stdlib.h>
#include <string.h>

int* maxMexArray(int* nums, int numsSize, int* returnSize) {
    int n = numsSize;
    int* remaining = calloc((size_t)(n + 2), sizeof(int));
    for (int i = 0; i < n; i++) if (nums[i] <= n + 1) remaining[nums[i]]++;
    int mex = 0;
    while (remaining[mex] > 0) mex++;
    int* answer = malloc((size_t)(n + 1) * sizeof(int));
    int an = 0;
    int* seen = calloc((size_t)(n + 2), sizeof(int));
    int stamp = 0, index = 0;
    while (index < n) {
        if (mex == 0) {
            answer[an++] = 0;
            int x = nums[index];
            if (x <= n + 1) remaining[x]--;
            index++;
            continue;
        }
        stamp++;
        int need = mex;
        while (need > 0) {
            int x = nums[index];
            if (x < mex && seen[x] != stamp) { seen[x] = stamp; need--; }
            if (x <= n + 1) remaining[x]--;
            index++;
        }
        answer[an++] = mex;
        mex = 0;
        while (remaining[mex] > 0) mex++;
    }
    free(remaining); free(seen);
    *returnSize = an;
    return answer;
}
