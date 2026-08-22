// LeetCode 3843 - First Element With Unique Frequency
// https://leetcode.com/problems/first-element-with-unique-frequency/

#include <stdlib.h>

int firstUniqueFreq(int* nums, int numsSize) {
    int* keys = (int*)malloc((size_t)numsSize * sizeof(int));
    int* cnt = (int*)calloc((size_t)numsSize, sizeof(int));
    int ksz = 0;
    for (int i = 0; i < numsSize; i++) {
        int found = -1;
        for (int j = 0; j < ksz; j++) if (keys[j] == nums[i]) { found = j; break; }
        if (found < 0) { keys[ksz] = nums[i]; cnt[ksz] = 1; ksz++; }
        else cnt[found]++;
    }
    int* freqKeys = (int*)malloc((size_t)ksz * sizeof(int));
    int* freqCnt = (int*)calloc((size_t)ksz, sizeof(int));
    int fsz = 0;
    for (int i = 0; i < ksz; i++) {
        int v = cnt[i];
        int found = -1;
        for (int j = 0; j < fsz; j++) if (freqKeys[j] == v) { found = j; break; }
        if (found < 0) { freqKeys[fsz] = v; freqCnt[fsz] = 1; fsz++; }
        else freqCnt[found]++;
    }
    int ans = -1;
    for (int i = 0; i < numsSize; i++) {
        int c = 0;
        for (int j = 0; j < ksz; j++) if (keys[j] == nums[i]) { c = cnt[j]; break; }
        int fc = 0;
        for (int j = 0; j < fsz; j++) if (freqKeys[j] == c) { fc = freqCnt[j]; break; }
        if (fc == 1) { ans = nums[i]; break; }
    }
    free(keys); free(cnt); free(freqKeys); free(freqCnt);
    return ans;
}
