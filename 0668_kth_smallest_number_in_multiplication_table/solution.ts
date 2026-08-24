// LeetCode 0668 - Kth Smallest Number in Multiplication Table
// https://leetcode.com/problems/kth-smallest-number-in-multiplication-table/

export function findKthNumber(m: number, n: number, k: number): number {
    const countLe = (x) => {
        let count = 0;
        for (let row = 1; row <= m; ++row) count += Math.min(Math.floor(x / row), n);
        return count;
    };
    let lo = 1, hi = m * n;
    while (lo < hi) {
        const mid = lo + Math.floor((hi - lo) / 2);
        if (countLe(mid) >= k) hi = mid;
        else lo = mid + 1;
    }
    return lo;
}
