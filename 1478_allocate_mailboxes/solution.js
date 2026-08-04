var minDistance = function(houses, k) {
    houses.sort((a, b) => a - b);
    const n = houses.length, cost = Array.from({ length: n }, () => Array(n).fill(0));
    for (let start = 0; start < n; start++) for (let end = start; end < n; end++) {
        const median = houses[Math.floor((start + end) / 2)];
        for (let i = start; i <= end; i++) cost[start][end] += Math.abs(houses[i] - median);
    }
    let dp = Array(n + 1).fill(Infinity);
    dp[0] = 0;
    for (let mailbox = 0; mailbox < k; mailbox++) {
        const next = Array(n + 1).fill(Infinity);
        next[0] = 0;
        for (let end = 1; end <= n; end++) {
            for (let start = 0; start < end; start++) {
                next[end] = Math.min(next[end], dp[start] + cost[start][end - 1]);
            }
        }
        dp = next;
    }
    return dp[n];
};
