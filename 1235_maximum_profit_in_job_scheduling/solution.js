// LeetCode 1235 - Maximum Profit in Job Scheduling
// https://leetcode.com/problems/maximum-profit-in-job-scheduling/

/**
 * @param {number[]} startTime
 * @param {number[]} endTime
 * @param {number[]} profit
 * @return {number}
 */
var jobScheduling = function(startTime, endTime, profit) {
    const jobs = endTime.map((end, i) => [end, startTime[i], profit[i]]).sort((a, b) => a[0] - b[0]);
    const ends = [0];
    const dp = [0];
    for (const [end, start, gain] of jobs) {
        let lo = 0, hi = ends.length - 1, idx = 0;
        while (lo <= hi) {
            const mid = (lo + hi) >> 1;
            if (ends[mid] <= start) {
                idx = mid;
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        ends.push(end);
        dp.push(Math.max(dp[dp.length - 1], dp[idx] + gain));
    }
    return dp[dp.length - 1];
};
