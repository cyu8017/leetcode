// LeetCode 3432 - Count Partitions With Even Sum Difference
// https://leetcode.com/problems/count-partitions-with-even-sum-difference/

int countPartitions(int* nums, int numsSize) {
    int total = 0;
    for (int i = 0; i < numsSize; i++) total += nums[i];
    int ans = 0, left = 0;
    for (int i = 0; i < numsSize - 1; i++) {
        left += nums[i];
        if ((left - (total - left)) % 2 == 0) ans++;
    }
    return ans;
}
