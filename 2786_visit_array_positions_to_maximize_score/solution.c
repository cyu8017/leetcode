// LeetCode 2786 - Visit Array Positions to Maximize Score
// https://leetcode.com/problems/visit-array-positions-to-maximize-score/

static long long max64(long long a, long long b) { return a > b ? a : b; }

long long maxScore(int* nums, int numsSize, int x) {
    long long NEG = -(1LL << 60);
    long long even = nums[0], odd = nums[0];
    if (nums[0] % 2 == 0) odd = NEG; else even = NEG;
    for (int i = 1; i < numsSize; i++) {
        long long v = nums[i];
        if (nums[i] % 2 == 0) even = max64(even + v, odd + v - x);
        else odd = max64(odd + v, even + v - x);
    }
    return max64(even, odd);
}
