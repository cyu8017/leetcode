// LeetCode 3113 - Find the Number of Subarrays Where Boundary Elements Are Maximum
// https://leetcode.com/problems/find-the-number-of-subarrays-where-boundary-elements-are-maximum/

#include <stdlib.h>

long long numberOfSubarrays(int* nums, int numsSize) {
    int* stk_v = (int*)malloc((size_t)numsSize * sizeof(int));
    int* stk_c = (int*)malloc((size_t)numsSize * sizeof(int));
    int top = 0;
    long long ans = 0;
    for (int i = 0; i < numsSize; i++) {
        int x = nums[i];
        while (top > 0 && stk_v[top - 1] < x) top--;
        if (top == 0 || stk_v[top - 1] > x) {
            stk_v[top] = x;
            stk_c[top] = 1;
            top++;
        } else {
            stk_c[top - 1]++;
        }
        ans += stk_c[top - 1];
    }
    free(stk_v); free(stk_c);
    return ans;
}
