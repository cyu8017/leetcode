// LeetCode 0581 - Shortest Unsorted Continuous Subarray
// https://leetcode.com/problems/shortest-unsorted-continuous-subarray/

int findUnsortedSubarray(int* nums, int numsSize) {
    int left = -1;
    int right = -2;
    int maxSeen = nums[0];
    int minSeen = nums[numsSize - 1];
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] > maxSeen) {
            maxSeen = nums[i];
        }
        if (nums[i] < maxSeen) {
            right = i;
        }
        int j = numsSize - 1 - i;
        if (nums[j] < minSeen) {
            minSeen = nums[j];
        }
        if (nums[j] > minSeen) {
            left = j;
        }
    }
    return right - left + 1;
}
