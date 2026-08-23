// LeetCode 3680 - Generate Schedule
// https://leetcode.com/problems/generate-schedule/

var generateSchedule = function(n) {
    if (n < 5) return [];
    const matches = [];
    for (let i = 0; i < n; i++)
        for (let j = 0; j < n; j++)
            if (i !== j) matches.push([i, j]);
    const used = new Array(matches.length).fill(false);
    const sched = [];
    let last0 = -1, last1 = -1;
    const dfs = () => {
        if (sched.length === matches.length) return true;
        for (let i = 0; i < matches.length; i++) {
            if (used[i]) continue;
            const m = matches[i];
            if (m[0] === last0 || m[0] === last1 || m[1] === last0 || m[1] === last1) continue;
            used[i] = true;
            sched.push(m);
            const p0 = last0, p1 = last1;
            last0 = m[0];
            last1 = m[1];
            if (dfs()) return true;
            last0 = p0;
            last1 = p1;
            sched.pop();
            used[i] = false;
        }
        return false;
    };
    if (dfs()) return sched;
    return [];
};
