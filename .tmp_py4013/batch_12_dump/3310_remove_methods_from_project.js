// LeetCode 3310 - Remove Methods From Project
// https://leetcode.com/problems/remove-methods-from-project/

var remainingMethods = function(n, k, invocations) {
    const g = Array.from({length: n}, () => []);
    for (const e of invocations) g[e[0]].push(e[1]);
    const sus = new Array(n).fill(false);
    const dfs = (u) => {
        if (sus[u]) return;
        sus[u] = true;
        for (const v of g[u]) dfs(v);
    };
    dfs(k);
    for (const e of invocations) {
        if (!sus[e[0]] && sus[e[1]]) {
            const ans = [];
            for (let i = 0; i < n; i++) ans.push(i);
            return ans;
        }
    }
    const ans = [];
    for (let i = 0; i < n; i++) if (!sus[i]) ans.push(i);
    return ans;
};
