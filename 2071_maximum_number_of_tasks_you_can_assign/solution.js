// LeetCode 2071 - Maximum Number of Tasks You Can Assign
// https://leetcode.com/problems/maximum-number-of-tasks-you-can-assign/

/**
 * @param {number[]} tasks
 * @param {number[]} workers
 * @param {number} pills
 * @param {number} strength
 * @return {number}
 */
var maxTaskAssign = function(tasks, workers, pills, strength) {
    tasks.sort((a, b) => a - b);
    workers.sort((a, b) => a - b);
    const remove = (ws, x) => {
        const c = ws.get(x);
        if (c === 1) ws.delete(x);
        else ws.set(x, c - 1);
    };
    const can = (k) => {
        if (k === 0) return true;
        const ws = new Map();
        for (let i = workers.length - k; i < workers.length; i++)
            ws.set(workers[i], (ws.get(workers[i]) || 0) + 1);
        let p = pills;
        const keys = () => [...ws.keys()].sort((a, b) => a - b);
        for (let i = k - 1; i >= 0; i--) {
            const task = tasks[i];
            const ks = keys();
            const strongest = ks[ks.length - 1];
            if (strongest >= task) {
                remove(ws, strongest);
                continue;
            }
            if (p === 0) return false;
            const need = task - strength;
            let found = null;
            for (const key of ks) if (key >= need) { found = key; break; }
            if (found === null) return false;
            remove(ws, found);
            p--;
        }
        return true;
    };
    let lo = 0, hi = Math.min(tasks.length, workers.length);
    while (lo < hi) {
        const mid = (lo + hi + 1) >> 1;
        if (can(mid)) lo = mid;
        else hi = mid - 1;
    }
    return lo;
};
