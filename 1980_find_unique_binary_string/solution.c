// LeetCode 1980 - Find Unique Binary String
// https://leetcode.com/problems/find-unique-binary-string/

#include <stdlib.h>
#include <string.h>

char* findDifferentBinaryString(char** nums, int numsSize) {
    char* res = (char*)malloc((size_t)numsSize + 1);
    for (int i = 0; i < numsSize; i++) {
        res[i] = nums[i][i] == '0' ? '1' : '0';
    }
    res[numsSize] = '\0';
    return res;
}
