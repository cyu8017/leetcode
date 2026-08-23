// LeetCode 3169 - Count Days Without Meetings
// https://leetcode.com/problems/count-days-without-meetings/

/**
 * @param {number} days
 * @param {number[][]} meetings
 * @return {number}
 */
var countDays = function(days, meetings) {
    meetings = meetings.slice().sort((a, b) => a[0] - b[0]);
    let last = 0, ans = 0;
    for (const e of meetings) {
        const st = e[0], ed = e[1];
        if (last < st) ans += st - last - 1;
        last = Math.max(last, ed);
    }
    ans += days - last;
    return ans;
};
