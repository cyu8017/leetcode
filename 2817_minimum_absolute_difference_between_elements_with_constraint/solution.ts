// LeetCode 2817 - Minimum Absolute Difference Between Elements With Constraint
// https://leetcode.com/problems/minimum-absolute-difference-between-elements-with-constraint/

export function minAbsoluteDifference(nums: number[], x: number): number {
    if (x === 0) {
        let ans0 = Number.MAX_SAFE_INTEGER;
        for (let i = 1; i < nums.length; i++)
            ans0 = Math.min(ans0, Math.abs(nums[i] - nums[i - 1]));
        return ans0;
    }
    let ans = Number.MAX_SAFE_INTEGER;
    const arr = [];
    const insert = (v) => {
        let lo = 0, hi = arr.length;
        while (lo < hi) {
            const mid = (lo + hi) >> 1;
            if (arr[mid] < v) lo = mid + 1;
            else hi = mid;
        }
        arr.splice(lo, 0, v);
    };
    const lowerBound = (v) => {
        let lo = 0, hi = arr.length;
        while (lo < hi) {
            const mid = (lo + hi) >> 1;
            if (arr[mid] < v) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    };
    for (let i = x; i < nums.length; i++) {
        insert(nums[i - x]);
        const cur = nums[i];
        const idx = lowerBound(cur);
        if (idx < arr.length) ans = Math.min(ans, arr[idx] - cur);
        if (idx > 0) ans = Math.min(ans, cur - arr[idx - 1]);
    }
    return ans;
}
