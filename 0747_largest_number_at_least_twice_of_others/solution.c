// LeetCode 0747 - Largest Number At Least Twice of Others
// https://leetcode.com/problems/largest-number-at-least-twice-of-others/

int dominantIndex(int* nums, int numsSize) {
    int first = -1, second = -1, index = -1;
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] > first) {
            second = first;
            first = nums[i];
            index = i;
        } else if (nums[i] > second) {
            second = nums[i];
        }
    }
    return first >= 2 * second ? index : -1;
}
