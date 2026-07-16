// LeetCode 0330 - Patching Array
// https://leetcode.com/problems/patching-array/

int minPatches(int* nums, int numsSize, int n) {
    int patches = 0;
    long long miss = 1;
    int index = 0;
    while (miss <= n) {
        if (index < numsSize && nums[index] <= miss) {
            miss += nums[index];
            index += 1;
        } else {
            miss += miss;
            patches += 1;
        }
    }
    return patches;
}
