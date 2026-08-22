// LeetCode 3701 - Compute Alternating Sum
// https://leetcode.com/problems/compute-alternating-sum/

int alternatingSum(int* nums, int numsSize) {
    int ans = 0;
    for (int i = 0; i < numsSize; i++) {
        if (i % 2 == 0) ans += nums[i];
        else ans -= nums[i];
    }
    return ans;
}
