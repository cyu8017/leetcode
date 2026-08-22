// LeetCode 3028 - Ant on the Boundary
// https://leetcode.com/problems/ant-on-the-boundary/

int returnToBoundaryCount(int* nums, int numsSize) {
    int s = 0, ans = 0;
    for (int i = 0; i < numsSize; i++) {
        s += nums[i];
        if (s == 0) ans++;
    }
    return ans;
}
