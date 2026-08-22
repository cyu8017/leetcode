// LeetCode 0376 - Wiggle Subsequence
// https://leetcode.com/problems/wiggle-subsequence/

int wiggleMaxLength(int* nums, int numsSize) {
    if (numsSize < 2) {
        return numsSize;
    }

    int up = 1;
    int down = 1;
    for (int index = 1; index < numsSize; index++) {
        if (nums[index] > nums[index - 1]) {
            up = down + 1;
        } else if (nums[index] < nums[index - 1]) {
            down = up + 1;
        }
    }

    return up > down ? up : down;
}
