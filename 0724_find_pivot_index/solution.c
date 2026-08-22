// LeetCode 0724 - Find Pivot Index
// https://leetcode.com/problems/find-pivot-index/

int pivotIndex(int* nums, int numsSize) {
    int total = 0;
    for (int i = 0; i < numsSize; i++) {
        total += nums[i];
    }
    int left = 0;
    for (int i = 0; i < numsSize; i++) {
        if (left == total - left - nums[i]) {
            return i;
        }
        left += nums[i];
    }
    return -1;
}
