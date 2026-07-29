// LeetCode 0673 - Number of Longest Increasing Subsequence
// https://leetcode.com/problems/number-of-longest-increasing-subsequence/

#include <stdlib.h>

int findNumberOfLIS(int* nums, int numsSize) {
    if (numsSize == 0) return 0;
    int* len = (int*)malloc((size_t)numsSize * sizeof(int));
    int* cnt = (int*)malloc((size_t)numsSize * sizeof(int));
    int maxLen = 0, answer = 0;
    for (int i = 0; i < numsSize; i++) {
        len[i] = 1; cnt[i] = 1;
        for (int j = 0; j < i; j++) {
            if (nums[j] < nums[i]) {
                if (len[j] + 1 > len[i]) { len[i] = len[j] + 1; cnt[i] = cnt[j]; }
                else if (len[j] + 1 == len[i]) cnt[i] += cnt[j];
            }
        }
        if (len[i] > maxLen) { maxLen = len[i]; answer = cnt[i]; }
        else if (len[i] == maxLen) answer += cnt[i];
    }
    free(len); free(cnt);
    return answer;
}
