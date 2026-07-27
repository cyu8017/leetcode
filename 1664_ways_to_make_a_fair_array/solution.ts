// LeetCode 1664 - Ways to Make a Fair Array
// https://leetcode.com/problems/ways-to-make-a-fair-array/

function waysToMakeFair(nums: number[]): number {
    let te = 0, to = 0;
    for (let i = 0; i < nums.length; i++) {
        if (i % 2) to += nums[i];
        else te += nums[i];
    }
    let le = 0, lo = 0, ans = 0;
    for (let i = 0; i < nums.length; i++) {
        const x = nums[i];
        if (i % 2) to -= x;
        else te -= x;
        if (le + to === lo + te) ans++;
        if (i % 2) lo += x;
        else le += x;
    }
    return ans;
}
