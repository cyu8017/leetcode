// LeetCode 2365 - Task Scheduler II
// https://leetcode.com/problems/task-scheduler-ii/

/**
 * @param {number[]} tasks
 * @param {number} space
 * @return {number}
 */
var taskSchedulerII = function(tasks, space) {
    const next = new Map();
    let day = 0;
    for (const t of tasks) {
        day = Math.max(day, next.get(t) || 0);
        day++;
        next.set(t, day + space);
    }
    return day;
};
