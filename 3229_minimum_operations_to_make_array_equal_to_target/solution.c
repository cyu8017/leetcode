// LeetCode 3229 - Minimum Operations to Make Array Equal to Target
// https://leetcode.com/problems/minimum-operations-to-make-array-equal-to-target/

static int abs3229(int x) { return x < 0 ? -x : x; }

long long minimumOperations(int* nums, int numsSize, int* target, int targetSize) {
    (void)targetSize;
    long long f = abs3229(target[0] - nums[0]);
    for (int i = 1; i < numsSize; i++) {
        int x = target[i] - nums[i];
        int y = target[i - 1] - nums[i - 1];
        if ((long long)x * y > 0) {
            int d = abs3229(x) - abs3229(y);
            if (d > 0) f += d;
        } else f += abs3229(x);
    }
    return f;
}
