// LeetCode 2589 - Minimum Time to Complete All Tasks
// https://leetcode.com/problems/minimum-time-to-complete-all-tasks/

/**
 * @param {number[][]} tasks
 * @return {number}
 */
var findMinimumTime = function(tasks) {
    tasks.sort((a, b) => a[1] - b[1]);
    const on = new Array(2001).fill(false);
    let ans = 0;
    for (const t of tasks) {
        const start = t[0], end = t[1], dur = t[2];
        let have = 0;
        for (let i = start; i <= end; ++i) if (on[i]) have++;
        let need = dur - have;
        for (let i = end; i >= start && need > 0; --i) {
            if (!on[i]) {
                on[i] = true;
                need--;
                ans++;
            }
        }
    }
    return ans;
};
