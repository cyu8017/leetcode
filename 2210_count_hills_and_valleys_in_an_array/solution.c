// LeetCode 2210 - Count Hills and Valleys in an Array
// https://leetcode.com/problems/count-hills-and-valleys-in-an-array/

#include <stdlib.h>

int countHillValley(int* nums, int numsSize) {
    int* compact = (int*)malloc((size_t)numsSize * sizeof(int));
    int cn = 0;
    compact[cn++] = nums[0];
    for (int i = 1; i < numsSize; i++)
        if (nums[i] != compact[cn - 1]) compact[cn++] = nums[i];
    int ans = 0;
    for (int i = 1; i + 1 < cn; i++) {
        if ((compact[i] > compact[i - 1] && compact[i] > compact[i + 1]) ||
            (compact[i] < compact[i - 1] && compact[i] < compact[i + 1]))
            ans++;
    }
    free(compact);
    return ans;
}
