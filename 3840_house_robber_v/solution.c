// LeetCode 3840 - House Robber V
// https://leetcode.com/problems/house-robber-v/

long long rob(int* nums, int numsSize, int* colors, int colorsSize) {
    (void)colorsSize;
    long long f = 0, g = nums[0];
    for (int i = 1; i < numsSize; i++) {
        long long nf, ng;
        if (colors[i - 1] == colors[i]) {
            nf = f > g ? f : g;
            ng = f + nums[i];
        } else {
            nf = f > g ? f : g;
            ng = nf + nums[i];
        }
        f = nf; g = ng;
    }
    return f > g ? f : g;
}
