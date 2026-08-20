"use strict";
// LeetCode 1376 - Time Needed To Inform All Employees
// https://leetcode.com/problems/time-needed-to-inform-all-employees/
function numOfMinutes(n, headID, manager, informTime) {
    const children = Array.from({ length: n }, (), any), any;
    [];
    ;
    for (let i = 0; i < n; i++)
        if (manager[i] !== -1)
            children[manager[i]].push(i);
    const dfs = (u) => {
        let best = 0;
        for (const v of children[u])
            best = Math.max(best, dfs(v));
        return informTime[u] + best;
    };
    return dfs(headID);
}
