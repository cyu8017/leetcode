// LeetCode 2931 - Maximum Spending After Buying Items
// https://leetcode.com/problems/maximum-spending-after-buying-items/

export function maxSpending(values: number[][]): number {
    const m = values.length, n = values[0].length;
    const idx = Array(m).fill(n - 1);
    let ans = 0, day = 1;
    const total = m * n;
    for (let t = 0; t < total; t++) {
        let bestI = -1, bestV = Number.MAX_SAFE_INTEGER;
        for (let i = 0; i < m; i++) {
            if (idx[i] >= 0 && values[i][idx[i]] < bestV) {
                bestV = values[i][idx[i]];
                bestI = i;
            }
        }
        ans += bestV * day;
        idx[bestI]--;
        day++;
    }
    return ans;
}
