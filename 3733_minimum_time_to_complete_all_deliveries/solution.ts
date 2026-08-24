// LeetCode 3733 - Minimum Time To Complete All Deliveries
// https://leetcode.com/problems/minimum_time_to_complete_all_deliveries/

export function minimumTime(d: any, r: any): any {
    const ok = (T) => {
        const w0 = T - Math.floor(T / r[0]);
        const w1 = T - Math.floor(T / r[1]);
        return w0 + w1 >= d[0] + d[1];
    };
    let lo = 1, hi = Number.MAX_SAFE_INTEGER;
    while (lo < hi) {
        const mid = lo + Math.floor((hi - lo) / 2);
        if (ok(mid)) hi = mid;
        else lo = mid + 1;
    }
    return lo;
}
