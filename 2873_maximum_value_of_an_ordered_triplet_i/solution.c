// LeetCode 2873 - Maximum Value of an Ordered Triplet I
// https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-i/

long long maximumTripletValue(int* nums, int numsSize) {
    long long ans = 0;
    for (int i = 0; i < numsSize; i++)
        for (int j = i + 1; j < numsSize; j++)
            for (int k = j + 1; k < numsSize; k++) {
                long long cand = (long long)(nums[i] - nums[j]) * nums[k];
                if (cand > ans) ans = cand;
            }
    return ans;
}
