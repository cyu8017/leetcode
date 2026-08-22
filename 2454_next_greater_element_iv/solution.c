// LeetCode 2454 - Next Greater Element IV
// https://leetcode.com/problems/next-greater-element-iv/

#include <stdlib.h>

int* secondGreaterElement(int* nums, int numsSize, int* returnSize) {
    int* ans = (int*)malloc((size_t)numsSize * sizeof(int));
    for (int i = 0; i < numsSize; i++) ans[i] = -1;
    int* stack1 = (int*)malloc((size_t)numsSize * sizeof(int));
    int* stack2 = (int*)malloc((size_t)numsSize * sizeof(int));
    int* tmp = (int*)malloc((size_t)numsSize * sizeof(int));
    int t1 = 0, t2 = 0;
    for (int i = 0; i < numsSize; i++) {
        int x = nums[i];
        while (t2 > 0 && nums[stack2[t2 - 1]] < x) {
            ans[stack2[--t2]] = x;
        }
        int tn = 0;
        while (t1 > 0 && nums[stack1[t1 - 1]] < x) {
            tmp[tn++] = stack1[--t1];
        }
        for (int j = tn - 1; j >= 0; j--) stack2[t2++] = tmp[j];
        stack1[t1++] = i;
    }
    free(stack1); free(stack2); free(tmp);
    *returnSize = numsSize;
    return ans;
}
