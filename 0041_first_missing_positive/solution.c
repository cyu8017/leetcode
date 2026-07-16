// LeetCode 0041 - First Missing Positive
// https://leetcode.com/problems/first-missing-positive/

int firstMissingPositive(int* nums, int numsSize) {
    int i = 0;

    while (i < numsSize) {
        int value = nums[i];
        int target = value - 1;
        if (value >= 1 && value <= numsSize && nums[target] != value) {
            int temp = nums[i];
            nums[i] = nums[target];
            nums[target] = temp;
        } else {
            i++;
        }
    }

    for (int index = 0; index < numsSize; index++) {
        if (nums[index] != index + 1) {
            return index + 1;
        }
    }

    return numsSize + 1;
}
