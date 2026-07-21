"use strict";
// LeetCode 1815 - Maximum Number of Groups Getting Fresh Donuts
// https://leetcode.com/problems/maximum-number-of-groups-getting-fresh-donuts/
function maxHappyGroups(batchSize, groups) {
    const count = new Array(batchSize).fill(0);
    for (const size of groups)
        count[size % batchSize] += 1;
    const memo = new Map();
    const dfs = (remainder, state) => {
        const key = remainder + '|' + state.join(',');
        if (memo.has(key))
            return memo.get(key);
        let best = 0;
        for (let mod = 1; mod < batchSize; mod++) {
            if (state[mod] === 0)
                continue;
            state[mod] -= 1;
            best = Math.max(best, dfs((remainder + mod) % batchSize, state));
            state[mod] += 1;
        }
        if (remainder === 0)
            best += 1;
        memo.set(key, best);
        return best;
    };
    let ans = dfs(0, count.slice());
    if (count[0])
        ans += count[0] - 1;
    return ans;
}
