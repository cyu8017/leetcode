// LeetCode 2432 - The Employee That Worked on the Longest Task
// https://leetcode.com/problems/the-employee-that-worked-on-the-longest-task/

/**
 * @param {number} n
 * @param {number[][]} logs
 * @return {number}
 */
var hardestWorker = function(n, logs) {
    let ans = logs[0][0], best = logs[0][1], prev = 0;
    for (const log of logs) {
        const dur = log[1] - prev;
        if (dur > best || (dur === best && log[0] < ans)) {
            best = dur;
            ans = log[0];
        }
        prev = log[1];
    }
    return ans;
};
