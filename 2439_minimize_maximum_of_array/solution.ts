// LeetCode 2439 - Minimize Maximum of Array
// https://leetcode.com/problems/minimize-maximum-of-array/

export function minimizeArrayValue(nums: number[]): number {
    let sum = 0, ans = 0;
    for (let i = 0; i < nums.length; i++) {
        sum += nums[i];
        const avg = Math.floor((sum + i) / (i + 1));
        if (avg > ans) ans = avg;
    }
    return ans;
}
