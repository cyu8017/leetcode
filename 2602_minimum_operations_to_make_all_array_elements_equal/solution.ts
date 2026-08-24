// LeetCode 2602 - Minimum Operations to Make All Array Elements Equal
// https://leetcode.com/problems/minimum-operations-to-make-all-array-elements-equal/

export function minOperations(nums: number[], queries: number[]): number[] {
    nums.sort((a, b) => a - b);
    const n = nums.length;
    const pref = new Array(n + 1).fill(0);
    for (let i = 0; i < n; ++i) pref[i + 1] = pref[i] + nums[i];
    const lowerBound = (x) => {
        let lo = 0, hi = n;
        while (lo < hi) {
            const mid = (lo + hi) >> 1;
            if (nums[mid] < x) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    };
    const ans = new Array(queries.length);
    for (let qi = 0; qi < queries.length; ++qi) {
        const q = queries[qi];
        const i = lowerBound(q);
        const left = q * i - pref[i];
        const right = pref[n] - pref[i] - q * (n - i);
        ans[qi] = left + right;
    }
    return ans;
}
