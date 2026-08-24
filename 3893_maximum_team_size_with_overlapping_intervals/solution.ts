// LeetCode 3893 - Maximum Team Size With Overlapping Intervals
// https://leetcode.com/problems/maximum-team-size-with-overlapping-intervals/

function UpperBound(a: any, x: any): any {
    let lo = 0, hi = a.length;
    while (lo < hi) {
        const mid = Math.floor((lo + hi) / 2);
        if (a[mid] <= x) lo = mid + 1;
        else hi = mid;
    }
    return lo;
}export function maximumTeamSize(startTime: any, endTime: any): any {
    const n = startTime.length;
    const st = startTime.slice().sort((a, b) => a - b);
    const en = endTime.slice().sort((a, b) => a - b);
    let ans = 0;
    for (let t = 0; t < n; t++) {
        const l = startTime[t], r = endTime[t];
        const i = UpperBound(en, l - 1);
        const j = UpperBound(st, r);
        ans = Math.max(ans, j - i);
    }
    return ans;
}
