// LeetCode 0453 - Minimum Moves to Equal Array Elements
// https://leetcode.com/problems/minimum-moves-to-equal-array-elements/

int minMoves(int* nums, int numsSize) {
    int minimum = nums[0];
    for (int i = 1; i < numsSize; i++) {
        if (nums[i] < minimum) {
            minimum = nums[i];
        }
    }
    int total = 0;
    for (int i = 0; i < numsSize; i++) {
        total += nums[i] - minimum;
    }
    return total;
}
