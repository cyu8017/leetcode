// LeetCode 3550 - Smallest Index With Digit Sum Equal to Index
// https://leetcode.com/problems/smallest-index-with-digit-sum-equal-to-index/

int smallestIndex(int* nums, int numsSize) {
    for (int i = 0; i < numsSize; i++) {
        int x = nums[i], s = 0;
        while (x > 0) { s += x % 10; x /= 10; }
        if (s == i) return i;
    }
    return -1;
}
