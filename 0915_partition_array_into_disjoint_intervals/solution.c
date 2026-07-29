// LeetCode 0915 - Partition Array into Disjoint Intervals
// https://leetcode.com/problems/partition-array-into-disjoint-intervals/

int partitionDisjoint(int* nums, int numsSize) {
    int leftMax = nums[0], curMax = nums[0], partition = 0;
    for (int i = 1; i < numsSize; i++) {
        if (nums[i] < leftMax) {
            leftMax = curMax;
            partition = i;
        } else if (nums[i] > curMax) {
            curMax = nums[i];
        }
    }
    return partition + 1;
}
