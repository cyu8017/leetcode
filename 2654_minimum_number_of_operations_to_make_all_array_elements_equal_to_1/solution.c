// LeetCode 2654 - Minimum Number of Operations to Make All Array Elements Equal to 1
// https://leetcode.com/problems/minimum-number-of-operations-to-make-all-array-elements-equal-to-1/

static int gcd2654(int a, int b) {
    while (b) { int t = a % b; a = b; b = t; }
    return a;
}

int minOperations(int* nums, int numsSize) {
    int ones = 0;
    for (int i = 0; i < numsSize; i++) if (nums[i] == 1) ones++;
    if (ones > 0) return numsSize - ones;
    int best = numsSize + 1;
    for (int i = 0; i < numsSize; i++) {
        int g = 0;
        for (int j = i; j < numsSize; j++) {
            g = gcd2654(g, nums[j]);
            if (g == 1) {
                if (j - i < best) best = j - i;
                break;
            }
        }
    }
    if (best == numsSize + 1) return -1;
    return best + numsSize - 1;
}
