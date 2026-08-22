// LeetCode 3736 - Minimum Moves to Equal Array Elements III
// https://leetcode.com/problems/minimum-moves-to-equal-array-elements-iii/

int minMoves(int* nums, int numsSize) {
    int mx = 0, s = 0;
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] > mx) mx = nums[i];
        s += nums[i];
    }
    return mx * numsSize - s;
}
