// LeetCode 0540 - Single Element in a Sorted Array
// https://leetcode.com/problems/single-element-in-a-sorted-array/

int singleNonDuplicate(int* nums, int numsSize) {
    int left = 0;
    int right = numsSize - 1;

    while (left < right) {
        int mid = (left + right) / 2;
        if (mid % 2 == 1) {
            mid--;
        }
        if (nums[mid] == nums[mid + 1]) {
            left = mid + 2;
        } else {
            right = mid;
        }
    }
    return nums[left];
}
