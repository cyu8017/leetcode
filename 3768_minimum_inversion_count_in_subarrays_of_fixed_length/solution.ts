// LeetCode 3768 - Minimum Inversion Count In Subarrays Of Fixed Length
// https://leetcode.com/problems/minimum_inversion_count_in_subarrays_of_fixed_length/

export function minInversionCount(nums: any, k: any): any {
    let vals = nums.slice().sort((a, b) => a - b);
    let n = 0;
    for (let i = 0; i < vals.length; i++) {
        if (n === 0 || vals[i] !== vals[n - 1]) vals[n++] = vals[i];
    }
    vals = vals.slice(0, n);
    const bit = new Array(vals.length + 1).fill(0);
    const add = (i, delta) => {
        for (; i < bit.length; i += i & -i) bit[i] += delta;
    };
    const sum = (i) => {
        let res = 0;
        for (; i > 0; i -= i & -i) res += bit[i];
        return res;
    };
    const lowerBound = (a, x) => {
        let lo = 0, hi = a.length;
        while (lo < hi) {
            const mid = (lo + hi) >> 1;
            if (a[mid] < x) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    };
    const rank = new Array(nums.length);
    let inv = 0;
    for (let i = 0; i < nums.length; i++) {
        rank[i] = lowerBound(vals, nums[i]) + 1;
        if (i < k) {
            inv += i - sum(rank[i]);
            add(rank[i], 1);
        }
    }
    let best = inv;
    for (let r = k; r < nums.length; r++) {
        const left = rank[r - k];
        inv -= sum(left - 1);
        add(left, -1);
        inv += k - 1 - sum(rank[r]);
        add(rank[r], 1);
        if (inv < best) best = inv;
    }
    return best;
}
