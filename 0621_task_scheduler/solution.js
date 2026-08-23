// LeetCode 0621 - Task Scheduler
// https://leetcode.com/problems/task-scheduler/

/**
 * @param {character[]} tasks
 * @param {number} n
 * @return {number}
 */
var leastInterval = function(tasks, n) {
    const counts = Array(26).fill(0);
    for (const task of tasks) ++counts[task.charCodeAt(0) - 65];
    let maxFreq = 0;
    for (const count of counts) maxFreq = Math.max(maxFreq, count);
    let maxCount = 0;
    for (const count of counts) if (count === maxFreq) ++maxCount;
    return Math.max(tasks.length, (maxFreq - 1) * (n + 1) + maxCount);
};
