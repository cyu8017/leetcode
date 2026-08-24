// LeetCode 3440 - Reschedule Meetings for Maximum Free Time II
// https://leetcode.com/problems/reschedule-meetings-for-maximum-free-time-ii/

var maxFreeTime = function(eventTime, startTime, endTime) {
    const n = startTime.length;
    const gaps = new Array(n + 1);
    gaps[0] = startTime[0];
    for (let i = 1; i < n; i++) gaps[i] = startTime[i] - endTime[i - 1];
    gaps[n] = eventTime - endTime[n - 1];
    let ans = 0;
    for (const g of gaps) if (g > ans) ans = g;
    const leftMax = new Array(n + 1), rightMax = new Array(n + 1);
    for (let i = 0; i <= n; i++) {
        leftMax[i] = gaps[i];
        if (i > 0 && leftMax[i - 1] > leftMax[i]) leftMax[i] = leftMax[i - 1];
    }
    for (let i = n; i >= 0; i--) {
        rightMax[i] = gaps[i];
        if (i < n && rightMax[i + 1] > rightMax[i]) rightMax[i] = rightMax[i + 1];
    }
    for (let i = 0; i < n; i++) {
        const dur = endTime[i] - startTime[i];
        const merged = gaps[i] + gaps[i + 1];
        let bestOther = 0;
        if (i > 0 && leftMax[i - 1] > bestOther) bestOther = leftMax[i - 1];
        if (i + 2 <= n && rightMax[i + 2] > bestOther) bestOther = rightMax[i + 2];
        let cand = merged;
        if (bestOther >= dur) cand = merged + dur;
        if (cand > ans) ans = cand;
    }
    return ans;
};
