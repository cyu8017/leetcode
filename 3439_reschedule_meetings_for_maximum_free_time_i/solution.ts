// LeetCode 3439 - Reschedule Meetings for Maximum Free Time I
// https://leetcode.com/problems/reschedule-meetings-for-maximum-free-time-i/

export function maxFreeTime(eventTime: any, k: any, startTime: any, endTime: any): any {
    const n = startTime.length;
    const gaps = new Array(n + 1);
    gaps[0] = startTime[0];
    for (let i = 1; i < n; i++) gaps[i] = startTime[i] - endTime[i - 1];
    gaps[n] = eventTime - endTime[n - 1];
    const window = k + 1;
    let sum = 0;
    for (let i = 0; i < window && i < gaps.length; i++) sum += gaps[i];
    let ans = sum;
    for (let i = window; i < gaps.length; i++) {
        sum += gaps[i] - gaps[i - window];
        if (sum > ans) ans = sum;
    }
    return ans;
}
