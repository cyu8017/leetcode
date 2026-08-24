// LeetCode 3862 - Find The Smallest Balanced Index
// https://leetcode.com/problems/find-the-smallest-balanced-index/

export function smallestBalancedIndex(nums: any): any {
    let s = 0, p = 1;
    for (const x of nums) s += x;
    for (let i = nums.length - 1; i >= 0; i--) {
        s -= nums[i];
        if (s === p) return i;
        p *= nums[i];
        if (p >= s) break;
    }
    return -1;
}
