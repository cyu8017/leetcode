// LeetCode 3487 - Maximum Unique Subarray Sum After Deletion
// https://leetcode.com/problems/maximum-unique-subarray-sum-after-deletion/

int maxSum(int* nums, int numsSize) {
    int seen[201] = {0};
    int sum = 0;
    int hasPos = 0;
    int maxNeg = -1000000000;
    for (int i = 0; i < numsSize; i++) {
        int x = nums[i];
        if (x < 0) {
            if (x > maxNeg) maxNeg = x;
            continue;
        }
        hasPos = 1;
        int idx = x + 100;
        if (!seen[idx]) {
            seen[idx] = 1;
            sum += x;
        }
    }
    if (hasPos) return sum;
    return maxNeg;
}
