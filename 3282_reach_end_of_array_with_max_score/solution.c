// LeetCode 3282 - Reach End of Array With Max Score
// https://leetcode.com/problems/reach-end-of-array-with-max-score/

long long findMaximumScore(int* nums, int numsSize) {
    long long ans = 0;
    int maxV = 0;
    for (int i = 0; i < numsSize - 1; i++) {
        if (nums[i] > maxV) maxV = nums[i];
        ans += maxV;
    }
    return ans;
}
