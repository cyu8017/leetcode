// LeetCode 1760 - Minimum Limit of Balls in a Bag
// https://leetcode.com/problems/minimum-limit-of-balls-in-a-bag/

int minimumSize(int* nums, int numsSize, int maxOperations) {
    int lo = 1;
    int hi = 0;
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] > hi) {
            hi = nums[i];
        }
    }
    while (lo < hi) {
        int mid = (lo + hi) / 2;
        long long ops = 0;
        for (int i = 0; i < numsSize; i++) {
            ops += (nums[i] - 1) / mid;
        }
        if (ops <= maxOperations) {
            hi = mid;
        } else {
            lo = mid + 1;
        }
    }
    return lo;
}
