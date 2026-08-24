// LeetCode 3180 - Maximum Total Reward Using Operations I
// https://leetcode.com/problems/maximum-total-reward-using-operations-i/

export function maxTotalReward(rewardValues: any): any {
    rewardValues.sort((a, b) => a - b);
    const n = rewardValues.length;
    const f = new Array(rewardValues[n - 1] << 1).fill(-1);
    const upperBound = (a, x) => {
        let lo = 0, hi = a.length;
        while (lo < hi) {
            const mid = (lo + hi) >> 1;
            if (a[mid] <= x) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    };
    const dfs = (x) => {
        if (f[x] !== -1) return f[x];
        const idx = upperBound(rewardValues, x);
        f[x] = 0;
        for (let it = idx; it < n; it++) {
            f[x] = Math.max(f[x], rewardValues[it] + dfs(x + rewardValues[it]));
        }
        return f[x];
    };
    return dfs(0);
}
