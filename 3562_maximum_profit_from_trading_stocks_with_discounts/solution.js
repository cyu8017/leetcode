// LeetCode 3562 - Maximum Profit from Trading Stocks with Discounts
// https://leetcode.com/problems/maximum-profit-from-trading-stocks-with-discounts/

var maxProfit = function(n, present, future, hierarchy, budget) {
    const g = Array.from({length: n + 1}, () => []);
    for (const e of hierarchy) g[e[0]].push(e[1]);
    function dfs(u) {
        const nxt = Array.from({length: budget + 1}, () => [0, 0]);
        for (const v of g[u]) {
            const fv = dfs(v);
            for (let j = budget; j >= 0; j--) {
                for (let jv = 0; jv <= j; jv++) {
                    for (let pre = 0; pre < 2; pre++) {
                        nxt[j][pre] = Math.max(nxt[j][pre], nxt[j - jv][pre] + fv[jv][pre]);
                    }
                }
            }
        }
        const f = Array.from({length: budget + 1}, () => [0, 0]);
        const price = future[u - 1];
        for (let j = 0; j <= budget; j++) {
            for (let pre = 0; pre < 2; pre++) {
                const cost = Math.floor(present[u - 1] / (pre + 1));
                if (j >= cost) {
                    const buyProfit = nxt[j - cost][1] + (price - cost);
                    f[j][pre] = Math.max(nxt[j][0], buyProfit);
                } else {
                    f[j][pre] = nxt[j][0];
                }
            }
        }
        return f;
    }
    return dfs(1)[budget][0];
};
