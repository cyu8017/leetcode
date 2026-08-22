// LeetCode 2023 - Number of Pairs of Strings With Concatenation Equal to Target
// https://leetcode.com/problems/number-of-pairs-of-strings-with-concatenation-equal-to-target/

#include <string.h>
#include <stdlib.h>
#include <stdio.h>

int numOfPairs(char** nums, int numsSize, char* target) {
    int ans = 0;
    int tlen = (int)strlen(target);
    for (int i = 0; i < numsSize; i++) {
        for (int j = 0; j < numsSize; j++) {
            if (i == j) continue;
            if ((int)strlen(nums[i]) + (int)strlen(nums[j]) != tlen) continue;
            char* buf = (char*)malloc((size_t)tlen + 1);
            strcpy(buf, nums[i]);
            strcat(buf, nums[j]);
            if (strcmp(buf, target) == 0) ans++;
            free(buf);
        }
    }
    return ans;
}
