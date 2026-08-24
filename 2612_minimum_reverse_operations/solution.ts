// LeetCode 2612 - Minimum Reverse Operations
// https://leetcode.com/problems/minimum-reverse-operations/

export function minReverseOperations(n: number, p: number, banned: number[], k: number): number[] {
    const ban = new Set(banned);
    const ans = new Array(n).fill(-1);
    ans[p] = 0;
    const q = [[p, 0]];
    while (q.length) {
        const cur = q.shift();
        const i = cur[0], d = cur[1];
        let lo = i - (k - 1);
        if (lo < 0) lo = 0;
        let hi = i;
        if (hi > n - k) hi = n - k;
        for (let L = lo; L <= hi; ++L) {
            const R = L + k - 1;
            const ni = L + R - i;
            if (ni < 0 || ni >= n || ban.has(ni) || ans[ni] !== -1) continue;
            ans[ni] = d + 1;
            q.push([ni, d + 1]);
        }
    }
    return ans;
}
