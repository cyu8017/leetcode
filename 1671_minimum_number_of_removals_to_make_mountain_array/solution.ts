// LeetCode 1671 - Minimum Number of Removals to Make Mountain Array
// https://leetcode.com/problems/minimum-number-of-removals-to-make-mountain-array/

function minimumMountainRemovals(nums: number[]): number {
    const lis = (a: number[]): number[] => {
        const d: number[] = [];
        const out: number[] = [];
        for (const x of a) {
            let lo = 0, hi = d.length;
            while (lo < hi) {
                const mid = (lo + hi) >> 1;
                if (d[mid] < x) lo = mid + 1;
                else hi = mid;
            }
            if (lo === d.length) d.push(x);
            else d[lo] = x;
            out.push(lo + 1);
        }
        return out;
    };
    const l = lis(nums);
    const r = lis(nums.slice().reverse()).reverse();
    const n = nums.length;
    let best = 0;
    for (let i = 0; i < n; i++) {
        if (l[i] > 1 && r[i] > 1) best = Math.max(best, l[i] + r[i] - 1);
    }
    return n - best;
}
