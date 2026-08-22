// LeetCode 1512 - Number of Good Pairs
// https://leetcode.com/problems/number-of-good-pairs/

int numIdenticalPairs(int* nums, int numsSize) {
    int count[101] = {0};
    int ans = 0;
    for (int i = 0; i < numsSize; i++) {
        ans += count[nums[i]];
        count[nums[i]]++;
    }
    return ans;
}
