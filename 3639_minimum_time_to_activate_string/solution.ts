// LeetCode 3639 - Minimum Time to Activate String
// https://leetcode.com/problems/minimum-time-to-activate-string/

export function minTime(s: any, order: any, k: any): any {
    const n = s.length;
    const total = n * (n + 1) / 2;
    if (k > total) return -1;
    const countValid = (t) => {
        const star = new Array(n).fill(false);
        for (let i = 0; i <= t; i++) star[order[i]] = true;
        let invalid = 0;
        for (let i = 0; i < n;) {
            if (star[i]) { i++; continue; }
            let j = i;
            while (j < n && !star[j]) j++;
            const L = j - i;
            invalid += L * (L + 1) / 2;
            i = j;
        }
        return total - invalid;
    };
    let lo = 0, hi = n - 1, ans = -1;
    while (lo <= hi) {
        const mid = (lo + hi) >> 1;
        if (countValid(mid) >= k) {
            ans = mid;
            hi = mid - 1;
        } else lo = mid + 1;
    }
    return ans;
}
