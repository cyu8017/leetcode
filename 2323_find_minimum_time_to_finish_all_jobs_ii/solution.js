// LeetCode 2323 - Find Minimum Time to Finish All Jobs II
// https://leetcode.com/problems/find-minimum-time-to-finish-all-jobs-ii/

/**
 * @param {number[]} jobs
 * @param {number[]} workers
 * @return {number}
 */
var minimumTime = function(jobs, workers) {
    jobs.sort((a, b) => a - b);
    workers.sort((a, b) => a - b);
    let ans = 0;
    for (let i = 0; i < jobs.length; ++i)
        ans = Math.max(ans, Math.floor((jobs[i] + workers[i] - 1) / workers[i]));
    return ans;
};
