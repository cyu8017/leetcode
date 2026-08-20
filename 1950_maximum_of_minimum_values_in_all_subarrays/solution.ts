// LeetCode 1950 - Maximum of Minimum Values in All Subarrays
// https://leetcode.com/problems/maximum-of-minimum-values-in-all-subarrays/

function findMaximums(nums: number[]): number[] {
    const n = nums.length;
    const left = new Array(n).fill(-1);
    const right = new Array(n).fill(n);
    let stack = [];
    for (let i = 0; i < n; i++) {
        while (stack.length && nums[stack[stack.length - 1]] >= nums[i]) stack.pop();
        left[i] = stack.length ? stack[stack.length - 1] : -1;
        stack.push(i);
    }
    stack = [];
    for (let i = n - 1; i >= 0; i--) {
        while (stack.length && nums[stack[stack.length - 1]] >= nums[i]) stack.pop();
        right[i] = stack.length ? stack[stack.length - 1] : n;
        stack.push(i);
    }
    const ans = new Array(n).fill(0);
    for (let i = 0; i < n; i++) {
        const length = right[i] - left[i] - 1;
        ans[length - 1] = Math.max(ans[length - 1], nums[i]);
    }
    for (let i = n - 2; i >= 0; i--) ans[i] = Math.max(ans[i], ans[i + 1]);
    return ans;
}
