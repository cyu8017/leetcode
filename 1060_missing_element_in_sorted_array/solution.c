// LeetCode 1060 - Missing Element in Sorted Array
// https://leetcode.com/problems/missing-element-in-sorted-array/

static int missing(int* nums, int i) {
    return nums[i] - nums[0] - i;
}

int missingElement(int* nums, int numsSize, int k) {
    if (k > missing(nums, numsSize - 1)) {
        return nums[numsSize - 1] + k - missing(nums, numsSize - 1);
    }
    int lo = 0, hi = numsSize - 1;
    while (lo < hi) {
        int mid = (lo + hi) / 2;
        if (missing(nums, mid) < k) {
            lo = mid + 1;
        } else {
            hi = mid;
        }
    }
    return nums[lo - 1] + k - missing(nums, lo - 1);
}
