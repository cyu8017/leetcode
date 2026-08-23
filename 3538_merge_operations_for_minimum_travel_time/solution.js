// LeetCode 3538 - Merge Operations for Minimum Travel Time
// https://leetcode.com/problems/merge-operations-for-minimum-travel-time/

var minTravelTime = function(l, n, k, position, time) {
    const prefix = new Array(n);
    prefix[0] = time[0];
    for (let i = 1; i < n; i++) prefix[i] = prefix[i - 1] + time[i];
    const memo = new Map();
    const INF = 1e18;
    function dp(i, skips, last) {
        if (i === n - 1) return skips === 0 ? 0 : INF;
        const key = i + ',' + skips + ',' + last;
        if (memo.has(key)) return memo.get(key);
        let rate = prefix[i];
        if (last > 0) rate -= prefix[last - 1];
        let res = INF;
        let end = n - 1;
        if (i + skips + 1 < end) end = i + skips + 1;
        for (let j = i + 1; j <= end; j++) {
            const cand = (position[j] - position[i]) * rate + dp(j, skips - (j - i - 1), i + 1);
            if (cand < res) res = cand;
        }
        memo.set(key, res);
        return res;
    }
    return dp(0, k, 0);
};
