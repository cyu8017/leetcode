// LeetCode 2626 - Array Reduce Transformation
// https://leetcode.com/problems/array-reduce-transformation/

typedef int (*ReduceFn)(int, int);

int reduce(int* nums, int numsSize, ReduceFn fn, int init) {
    int acc = init;
    for (int i = 0; i < numsSize; i++) acc = fn(acc, nums[i]);
    return acc;
}
