// LeetCode 2702 - Minimum Operations to Make Numbers Non-positive
// https://leetcode.com/problems/minimum-operations-to-make-numbers-non-positive/

static int ok2702(int* nums, int n, int x, int y, int ops) {
    long long extra = 0;
    for (int i = 0; i < n; i++) {
        long long remain = (long long)nums[i] - (long long)ops * y;
        if (remain > 0)
            extra += (remain + (x - y) - 1) / (x - y);
    }
    return extra <= ops;
}

int minOperations(int* nums, int numsSize, int x, int y) {
    int lo = 0, hi = 0;
    for (int i = 0; i < numsSize; i++) {
        int a = (nums[i] + y - 1) / y;
        int b = (nums[i] + x - 1) / x;
        if (a > hi) hi = a;
        if (b > hi) hi = b;
    }
    hi += numsSize;
    while (lo < hi) {
        int mid = (lo + hi) / 2;
        if (ok2702(nums, numsSize, x, y, mid)) hi = mid;
        else lo = mid + 1;
    }
    return lo;
}
