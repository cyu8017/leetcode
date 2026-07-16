// LeetCode 0035 - Search Insert Position
// https://leetcode.com/problems/search-insert-position/

int searchInsert(int* nums, int numsSize, int target) {
    int left = 0;
    int right = numsSize;

    while (left < right) {
        int mid = left + (right - left) / 2;
        if (nums[mid] < target) {
            left = mid + 1;
        } else {
            right = mid;
        }
    }

    return left;
}
