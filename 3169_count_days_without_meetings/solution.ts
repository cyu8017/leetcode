// LeetCode 3169 - Count Days Without Meetings
// https://leetcode.com/problems/count-days-without-meetings/

export function countDays(days: number, meetings: number[][]): number {
    meetings = meetings.slice().sort((a, b) => a[0] - b[0]);
    let last = 0, ans = 0;
    for (const e of meetings) {
        const st = e[0], ed = e[1];
        if (last < st) ans += st - last - 1;
        last = Math.max(last, ed);
    }
    ans += days - last;
    return ans;
}
