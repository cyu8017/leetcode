// LeetCode 3344 - Maximum Sized Array
// https://leetcode.com/problems/maximum-sized-array/

function ok(n: any, s: any): any {
    let sum = 0;
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
            const ij = i | j;
            sum += ij * (n - 1) * n / 2;
            if (sum > s) return false;
        }
    }
    return sum <= s;
}export function maxSizedArray(s: any): any {
    let lo = 1, hi = 2000;
    while (lo < hi) {
        const mid = Math.floor((lo + hi + 1) / 2);
        if (ok(mid, s)) lo = mid;
        else hi = mid - 1;
    }
    return lo;
}
