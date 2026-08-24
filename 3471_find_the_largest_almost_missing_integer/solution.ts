// LeetCode 3471 - Find the Largest Almost Missing Integer
// https://leetcode.com/problems/find-the-largest-almost-missing-integer/

export function largestInteger(nums: any, k: any): any {
    const n = nums.length;
    const cnt = new Map();
    for (let i = 0; i + k <= n; i++) {
        const seen = new Set();
        for (let j = i; j < i + k; j++) seen.add(nums[j]);
        for (const x of seen) cnt.set(x, (cnt.get(x) || 0) + 1);
    }
    let ans = -1;
    for (const [key, value] of cnt) {
        if (value === 1 && key > ans) ans = key;
    }
    return ans;
}
