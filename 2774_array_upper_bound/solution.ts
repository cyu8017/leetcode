// LeetCode 2774 - Array Upper Bound
// https://leetcode.com/problems/array-upper-bound/

export function upperBound(self: any[], target: number): number {
    let lo = 0, hi = self.length;
    while (lo < hi) {
        const mid = (lo + hi) >> 1;
        if (self[mid] <= target) lo = mid + 1;
        else hi = mid;
    }
    if (lo === 0 || self[lo - 1] !== target) return -1;
    return lo - 1;
}
