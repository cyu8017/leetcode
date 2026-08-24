// LeetCode 3318 - Find X-Sum of All K-Long Subarrays I
// https://leetcode.com/problems/find-x-sum-of-all-k-long-subarrays-i/

export function findXSum(nums: any, k: any, x: any): any {
    const n = nums.length;
    const ans = new Array(n - k + 1);
    for (let i = 0; i <= n - k; i++) {
        const freq = new Map();
        for (let j = i; j < i + k; j++) freq.set(nums[j], (freq.get(nums[j]) || 0) + 1);
        const arr = [];
        for (const [key, val] of freq) arr.push([key, val]);
        arr.sort((A, B) => B[1] !== A[1] ? B[1] - A[1] : B[0] - A[0]);
        const lim = Math.min(x, arr.length);
        const keep = new Set();
        for (let t = 0; t < lim; t++) keep.add(arr[t][0]);
        let sum = 0;
        for (let j = i; j < i + k; j++) if (keep.has(nums[j])) sum += nums[j];
        ans[i] = sum;
    }
    return ans;
}
