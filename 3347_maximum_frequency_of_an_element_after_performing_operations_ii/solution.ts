// LeetCode 3347 - Maximum Frequency of an Element After Performing Operations II
// https://leetcode.com/problems/maximum-frequency-of-an-element-after-performing-operations-ii/

function lowerBound(a: any, x: any): any {
    let lo = 0, hi = a.length;
    while (lo < hi) {
        const mid = (lo + hi) >> 1;
        if (a[mid] < x) lo = mid + 1; else hi = mid;
    }
    return lo;
}function upperBound(a: any, x: any): any {
    let lo = 0, hi = a.length;
    while (lo < hi) {
        const mid = (lo + hi) >> 1;
        if (a[mid] <= x) lo = mid + 1; else hi = mid;
    }
    return lo;
}export function maxFrequency(nums: any, k: any, numOperations: any): any {
    nums.sort((a, b) => a - b);
    const freq = new Map();
    for (const x of nums) freq.set(x, (freq.get(x) || 0) + 1);
    let ans = 1;
    const candidates = [];
    const seen = new Set();
    for (const x of nums) {
        for (const t of [x - k, x, x + k]) {
            if (!seen.has(t)) { seen.add(t); candidates.push(t); }
        }
    }
    for (const t of candidates) {
        const lo = lowerBound(nums, t - k);
        const hi = upperBound(nums, t + k);
        const can = hi - lo;
        const f = freq.get(t) || 0;
        const use = Math.min(can, f + numOperations);
        if (use > ans) ans = use;
    }
    return ans;
}
