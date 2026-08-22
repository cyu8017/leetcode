// LeetCode 0213 - House Robber II
// https://leetcode.com/problems/house-robber-ii/

static int robLinear(int* nums, int start, int end) {
    int previousTwo = 0;
    int previousOne = 0;
    for (int i = start; i < end; ++i) {
        const int current = previousOne > previousTwo + nums[i]
            ? previousOne
            : previousTwo + nums[i];
        previousTwo = previousOne;
        previousOne = current;
    }
    return previousOne;
}

int rob(int* nums, int numsSize) {
    if (numsSize == 1) {
        return nums[0];
    }
    const int withoutLast = robLinear(nums, 0, numsSize - 1);
    const int withoutFirst = robLinear(nums, 1, numsSize);
    return withoutLast > withoutFirst ? withoutLast : withoutFirst;
}
