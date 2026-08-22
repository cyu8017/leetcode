// LeetCode 2057 - Smallest Index With Equal Value
// https://leetcode.com/problems/smallest-index-with-equal-value/

int smallestEqual(int* nums, int numsSize) {
    for (int i = 0; i < numsSize; i++) if (i % 10 == nums[i]) return i;
    return -1;
}
