// LeetCode 1330 - Reverse Subarray To Maximize Array Value
// https://leetcode.com/problems/reverse-subarray-to-maximize-array-value/

int maxValueAfterReverse(int* nums, int numsSize) {
    int base = 0;
    for (int i = 0; i + 1 < numsSize; i++) {
        int d = nums[i] - nums[i + 1];
        base += d < 0 ? -d : d;
    }
    int gain = 0;
    int low = 1000000000, high = -1000000000;
    for (int i = 0; i + 1 < numsSize; i++) {
        int a = nums[i], b = nums[i + 1];
        int ab = a - b; if (ab < 0) ab = -ab;
        int g1 = nums[0] - b; if (g1 < 0) g1 = -g1; g1 -= ab;
        int g2 = nums[numsSize - 1] - a; if (g2 < 0) g2 = -g2; g2 -= ab;
        if (g1 > gain) gain = g1;
        if (g2 > gain) gain = g2;
        int mx = a > b ? a : b;
        int mn = a < b ? a : b;
        if (mx < low) low = mx;
        if (mn > high) high = mn;
    }
    int g3 = 2 * (high - low);
    if (g3 > gain) gain = g3;
    return base + gain;
}
