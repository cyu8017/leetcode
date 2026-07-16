// LeetCode 0080 - Remove Duplicates from Sorted Array II
// https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

int removeDuplicates(int* nums, int numsSize) {
    if (numsSize <= 2) {
        return numsSize;
    }

    int write = 2;
    for (int i = 2; i < numsSize; i++) {
        if (nums[i] != nums[write - 2]) {
            nums[write] = nums[i];
            write++;
        }
    }

    return write;
}
