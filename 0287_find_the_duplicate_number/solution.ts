// LeetCode 0287 - Find the Duplicate Number
// https://leetcode.com/problems/find-the-duplicate-number/

export function findDuplicate(nums: number[]): number {
    let slow = nums[0];
    let fast = nums[0];
    while (true) {
        slow = nums[slow];
        fast = nums[nums[fast]];
        if (slow === fast) {
            break;
        }
    }
    slow = nums[0];
    while (slow !== fast) {
        slow = nums[slow];
        fast = nums[fast];
    }
    return slow;
}
