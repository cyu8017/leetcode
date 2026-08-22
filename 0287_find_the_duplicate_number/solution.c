// LeetCode 0287 - Find the Duplicate Number
// https://leetcode.com/problems/find-the-duplicate-number/

int findDuplicate(int* nums, int numsSize) {
    int slow = nums[0];
    int fast = nums[0];
    while (1) {
        slow = nums[slow];
        fast = nums[nums[fast]];
        if (slow == fast) {
            break;
        }
    }
    slow = nums[0];
    while (slow != fast) {
        slow = nums[slow];
        fast = nums[fast];
    }
    return slow;
}
