// LeetCode 1133 - Largest Unique Number
// https://leetcode.com/problems/largest-unique-number/

int largestUniqueNumber(int* nums, int numsSize) {
    int count[1001] = {0};
    for (int i = 0; i < numsSize; i++) count[nums[i]]++;
    for (int v = 1000; v >= 0; v--) if (count[v] == 1) return v;
    return -1;
}
