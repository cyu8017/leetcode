// LeetCode 3423 - Maximum Difference Between Adjacent Elements in a Circular Array
// https://leetcode.com/problems/maximum-difference-between-adjacent-elements-in-a-circular-array/

export function maxAdjacentDistance(nums: any): any {
    let ans = 0;
    const n = nums.length;
    for (let i = 0; i < n; i++) {
        const d = Math.abs(nums[i] - nums[(i + 1) % n]);
        if (d > ans) ans = d;
    }
    return ans;
}
