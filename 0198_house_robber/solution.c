// LeetCode 0198 - House Robber
// https://leetcode.com/problems/house-robber/

int rob(int* nums, int numsSize) {
    int previous_two = 0;
    int previous_one = 0;
    for (int i = 0; i < numsSize; ++i) {
        const int current = previous_one > previous_two + nums[i]
            ? previous_one
            : previous_two + nums[i];
        previous_two = previous_one;
        previous_one = current;
    }
    return previous_one;
}
