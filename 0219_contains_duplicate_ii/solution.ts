// LeetCode 0219 - Contains Duplicate II
// https://leetcode.com/problems/contains-duplicate-ii/

export function containsNearbyDuplicate(nums: number[], k: number): boolean {
    const lastIndex = new Map<number, number>();
    for (let i = 0; i < nums.length; i++) {
        const num = nums[i];
        if (lastIndex.has(num) && i - lastIndex.get(num)! <= k) {
            return true;
        }
        lastIndex.set(num, i);
    }
    return false;
}
