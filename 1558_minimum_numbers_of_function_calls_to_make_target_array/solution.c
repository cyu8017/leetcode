// LeetCode 1558 - Minimum Numbers of Function Calls to Make Target Array
// https://leetcode.com/problems/minimum-numbers-of-function-calls-to-make-target-array/

int minOperations(int* nums, int numsSize) {
    int adds = 0, maxMul = 0;
    for (int i = 0; i < numsSize; i++) {
        int x = nums[i], bits = 0, mul = 0;
        while (x) {
            if (x & 1) bits++;
            x >>= 1;
            if (x) mul++;
        }
        adds += bits;
        if (mul > maxMul) maxMul = mul;
    }
    return adds + maxMul;
}
