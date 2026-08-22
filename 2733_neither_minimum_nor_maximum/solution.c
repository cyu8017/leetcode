// LeetCode 2733 - Neither Minimum nor Maximum
// https://leetcode.com/problems/neither-minimum-nor-maximum/

int findNonMinOrMax(int* nums, int numsSize) {
    if (numsSize < 3) return -1;
    int a = nums[0], b = nums[1], c = nums[2];
    if ((a - b) * (a - c) <= 0) return a;
    if ((b - a) * (b - c) <= 0) return b;
    return c;
}
