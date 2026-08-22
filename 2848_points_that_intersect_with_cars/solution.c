// LeetCode 2848 - Points That Intersect With Cars
// https://leetcode.com/problems/points-that-intersect-with-cars/

int numberOfPoints(int** nums, int numsSize, int* numsColSize) {
    (void)numsColSize;
    int cov[102] = {0};
    for (int i = 0; i < numsSize; i++) {
        for (int x = nums[i][0]; x <= nums[i][1]; x++) cov[x] = 1;
    }
    int ans = 0;
    for (int i = 0; i < 102; i++) ans += cov[i];
    return ans;
}
