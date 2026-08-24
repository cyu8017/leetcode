// LeetCode 2244 - Minimum Rounds to Complete All Tasks
// https://leetcode.com/problems/minimum-rounds-to-complete-all-tasks/

/**
 * @param {number[]} tasks
 * @return {number}
 */
var minimumRounds = function(tasks) {
    const freq = new Map();
    for (const t of tasks) freq.set(t, (freq.get(t) || 0) + 1);
    let ans = 0;
    for (const c of freq.values()) {
        if (c === 1) return -1;
        ans += Math.floor((c + 2) / 3);
    }
    return ans;
};
