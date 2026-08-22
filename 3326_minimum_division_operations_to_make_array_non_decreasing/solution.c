// LeetCode 3326 - Minimum Division Operations to Make Array Non Decreasing
// https://leetcode.com/problems/minimum-division-operations-to-make-array-non-decreasing/

static int smallestProperDivisor(int x) {
    for (int d = 2; (long long)d * d <= x; d++) if (x % d == 0) return d;
    return x;
}

int minOperations(int* nums, int numsSize) {
    int ops = 0;
    for (int i = numsSize - 2; i >= 0; i--) {
        if (nums[i] <= nums[i + 1]) continue;
        while (nums[i] > nums[i + 1]) {
            int d = smallestProperDivisor(nums[i]);
            if (d == nums[i]) return -1;
            nums[i] /= d;
            ops++;
            if (nums[i] > nums[i + 1] && smallestProperDivisor(nums[i]) == nums[i]) return -1;
        }
    }
    return ops;
}
