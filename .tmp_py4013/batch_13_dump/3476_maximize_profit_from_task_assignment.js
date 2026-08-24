// LeetCode 3476 - Maximize Profit from Task Assignment
// https://leetcode.com/problems/maximize-profit-from-task-assignment/

var maxProfit = function(workers, tasks) {
    workers = workers.slice().sort((a, b) => a - b);
    tasks = tasks.slice().sort((a, b) => a[0] - b[0]);
    let ans = 0;
    const used = new Array(tasks.length).fill(false);
    for (const w of workers) {
        let best = -1, bi = -1;
        for (let i = 0; i < tasks.length; i++) {
            if (used[i]) continue;
            if (tasks[i][0] > w) break;
            if (tasks[i][1] > best) {
                best = tasks[i][1];
                bi = i;
            }
        }
        if (bi >= 0) {
            used[bi] = true;
            ans += best;
        }
    }
    return ans;
};
