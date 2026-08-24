// LeetCode 3073 - Maximum Increasing Triplet Value
// https://leetcode.com/problems/maximum-increasing-triplet-value/

export function maximumTripletValue(nums: number[]): number {
    const n = nums.length;
    const right = new Array(n);
    right[n - 1] = nums[n - 1];
    for (let i = n - 2; i >= 0; i--) right[i] = Math.max(nums[i], right[i + 1]);
    // Sorted unique list simulating TreeSet.lower
    const ts = [];
    const add = (x) => {
        let lo = 0, hi = ts.length;
        while (lo < hi) {
            const mid = (lo + hi) >> 1;
            if (ts[mid] < x) lo = mid + 1;
            else hi = mid;
        }
        if (lo === ts.length || ts[lo] !== x) ts.splice(lo, 0, x);
    };
    const lower = (x) => {
        let lo = 0, hi = ts.length;
        while (lo < hi) {
            const mid = (lo + hi) >> 1;
            if (ts[mid] < x) lo = mid + 1;
            else hi = mid;
        }
        return lo > 0 ? ts[lo - 1] : null;
    };
    add(nums[0]);
    let ans = 0;
    for (let j = 1; j < n - 1; j++) {
        if (right[j + 1] > nums[j]) {
            const it = lower(nums[j]);
            if (it !== null) ans = Math.max(ans, it - nums[j] + right[j + 1]);
        }
        add(nums[j]);
    }
    return ans;
}
