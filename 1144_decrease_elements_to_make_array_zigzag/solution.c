// LeetCode 1144 - Decrease Elements To Make Array Zigzag
// https://leetcode.com/problems/decrease-elements-to-make-array-zigzag/

static int zigzagCost(int* nums, int numsSize, int start) {
    int ans = 0;
    for (int i = start; i < numsSize; i += 2) {
        int left = i ? nums[i - 1] : 2147483647;
        int right = i + 1 < numsSize ? nums[i + 1] : 2147483647;
        int lim = left < right ? left : right;
        if (nums[i] >= lim) ans += nums[i] - lim + 1;
    }
    return ans;
}

int movesToMakeZigzag(int* nums, int numsSize) {
    int a = zigzagCost(nums, numsSize, 0);
    int b = zigzagCost(nums, numsSize, 1);
    return a < b ? a : b;
}
