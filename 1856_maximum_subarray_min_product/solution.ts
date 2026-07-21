// LeetCode 1856 - Maximum Subarray Min-Product
// https://leetcode.com/problems/maximum-subarray-min-product/

function maxSumMinProduct(nums: number[]): number {
    const mod = 1e9 + 7;
    const n = nums.length;
    const prefix = new Array(n + 1).fill(0);
    for (let i = 0; i < n; i++) prefix[i + 1] = prefix[i] + nums[i];

    const leftBound = new Array(n).fill(-1);
    const stack: number[] = [];
    for (let i = 0; i < n; i++) {
        while (stack.length && nums[stack[stack.length - 1]] >= nums[i]) stack.pop();
        leftBound[i] = stack.length ? stack[stack.length - 1] : -1;
        stack.push(i);
    }

    const rightBound = new Array(n).fill(n);
    stack.length = 0;
    for (let i = n - 1; i >= 0; i--) {
        while (stack.length && nums[stack[stack.length - 1]] >= nums[i]) stack.pop();
        rightBound[i] = stack.length ? stack[stack.length - 1] : n;
        stack.push(i);
    }

    let best = 0;
    for (let i = 0; i < n; i++) {
        const total = prefix[rightBound[i]] - prefix[leftBound[i] + 1];
        best = Math.max(best, total * nums[i]);
    }
    return best % mod;
}
