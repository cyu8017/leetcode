// LeetCode 2855 - Minimum Right Shifts to Sort the Array
// https://leetcode.com/problems/minimum-right-shifts-to-sort-the-array/

int minimumRightShifts(int* nums, int numsSize) {
    int n = numsSize, drops = 0, idx = -1;
    for (int i = 0; i < n; i++) {
        if (nums[i] > nums[(i + 1) % n]) { drops++; idx = i; }
    }
    if (drops == 0) return 0;
    if (drops > 1) return -1;
    return n - 1 - idx;
}
