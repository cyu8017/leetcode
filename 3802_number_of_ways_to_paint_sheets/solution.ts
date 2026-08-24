// LeetCode 3802 - Number Of Ways To Paint Sheets
// https://leetcode.com/problems/number_of_ways_to_paint_sheets/

export function numberOfWays(n: any, limit: any): any {
    const MOD = 1000000007;
    limit = limit.slice().sort((a, b) => a - b);
    let points = [1, n];
    for (const x of limit) {
        if (x + 1 > 1 && x + 1 < n) points.push(x + 1);
        if (n - x > 1 && n - x < n) points.push(n - x);
    }
    points.sort((a, b) => a - b);
    let u = 0;
    for (let i = 0; i < points.length; i++) {
        if (u === 0 || points[i] !== points[u - 1]) points[u++] = points[i];
    }
    points = points.slice(0, u);
    const countGE = (lim, x) => {
        let lo = 0, hi = lim.length;
        while (lo < hi) {
            const mid = (lo + hi) >> 1;
            if (lim[mid] < x) lo = mid + 1;
            else hi = mid;
        }
        return lim.length - lo;
    };
    let ans = 0;
    for (let i = 0; i + 1 < points.length; i++) {
        const x = points[i];
        const a = countGE(limit, x), b = countGE(limit, n - x);
        const same = countGE(limit, Math.max(x, n - x));
        let ways = (a * b - same) % MOD;
        const length = points[i + 1] - x;
        ans = (ans + ways * length) % MOD;
    }
    if (ans < 0) ans += MOD;
    return ans;
}
