// LeetCode 2054 - Two Best Non-Overlapping Events
// https://leetcode.com/problems/two-best-non-overlapping-events/

export function maxTwoEvents(events: number[][]): number {
    events.sort((a, b) => a[0] - b[0]);
    const n = events.length;
    const suffix = new Array(n + 1).fill(0);
    for (let i = n - 1; i >= 0; i--) suffix[i] = Math.max(suffix[i + 1], events[i][2]);
    let ans = 0;
    for (let i = 0; i < n; i++) {
        ans = Math.max(ans, events[i][2]);
        let lo = i + 1, hi = n;
        while (lo < hi) {
            const mid = (lo + hi) >> 1;
            if (events[mid][0] > events[i][1]) hi = mid;
            else lo = mid + 1;
        }
        if (lo < n) ans = Math.max(ans, events[i][2] + suffix[lo]);
    }
    return ans;
}
