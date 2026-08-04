var minCost = function(houses, cost, m, n, target) {
    const inf = Infinity;
    let dp = Array.from({ length: n + 1 }, () => Array(target + 1).fill(inf));
    dp[0][0] = 0;
    for (let i = 0; i < m; i++) {
        const next = Array.from({ length: n + 1 }, () => Array(target + 1).fill(inf));
        for (let previous = 0; previous <= n; previous++) for (let groups = 0; groups <= target; groups++) {
            if (dp[previous][groups] === inf) continue;
            const colors = houses[i] ? [houses[i]] : Array.from({ length: n }, (_, c) => c + 1);
            for (const color of colors) {
                const newGroups = groups + (color !== previous ? 1 : 0);
                if (newGroups <= target) {
                    next[color][newGroups] = Math.min(next[color][newGroups],
                        dp[previous][groups] + (houses[i] ? 0 : cost[i][color - 1]));
                }
            }
        }
        dp = next;
    }
    const answer = Math.min(...dp.map(row => row[target]));
    return answer === inf ? -1 : answer;
};
