// LeetCode 3190 - Find Minimum Operations to Make All Elements Divisible by Three
// https://leetcode.com/problems/find-minimum-operations-to-make-all-elements-divisible-by-three/

int minimumOperations(int* nums, int numsSize) {
    int ans = 0;
    for (int i = 0; i < numsSize; i++) if (nums[i] % 3 != 0) ans++;
    return ans;
}
