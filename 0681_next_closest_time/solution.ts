// LeetCode 0681 - Next Closest Time
// https://leetcode.com/problems/next-closest-time/

export function nextClosestTime(time: string): string {
    const digits = new Set([time[0], time[1], time[3], time[4]]);
    const start = parseInt(time.substring(0, 2), 10) * 60 + parseInt(time.substring(3, 5), 10);
    for (let delta = 1; delta <= 24 * 60; delta++) {
        const mins = (start + delta) % (24 * 60);
        const hh = Math.floor(mins / 60), mm = mins % 60;
        const c0 = String(Math.floor(hh / 10));
        const c1 = String(hh % 10);
        const c2 = String(Math.floor(mm / 10));
        const c3 = String(mm % 10);
        if (digits.has(c0) && digits.has(c1) && digits.has(c2) && digits.has(c3)) {
            return c0 + c1 + ':' + c2 + c3;
        }
    }
    return time;
}
