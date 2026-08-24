// LeetCode 2406 - Divide Intervals Into Minimum Number of Groups
// https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups/

export function minGroups(intervals: number[][]): number {
    const events = [];
    for (const it of intervals) {
        events.push([it[0], 1]);
        events.push([it[1] + 1, -1]);
    }
    events.sort((a, b) => a[0] !== b[0] ? a[0] - b[0] : a[1] - b[1]);
    let cur = 0, ans = 0;
    for (const e of events) {
        cur += e[1];
        ans = Math.max(ans, cur);
    }
    return ans;
}
