// LeetCode 3669 - Balanced K-Factor Decomposition
// https://leetcode.com/problems/balanced-k-factor-decomposition/

export function minDifference(n: any, k: any): any {
    const MX = 100001;
    if (!minDifference._g) {
        const g = Array.from({length: MX}, () => []);
        for (let i = 1; i < MX; i++)
            for (let j = i; j < MX; j += i) g[j].push(i);
        minDifference._g = g;
    }
    const g = minDifference._g;
    let cur = Infinity;
    let ans = [];
    const path = new Array(k);
    const dfs = (i, x, mi, mx) => {
        if (i === 0) {
            const d = Math.max(mx, x) - Math.min(mi, x);
            if (d < cur) {
                cur = d;
                path[i] = x;
                ans = path.slice();
            }
            return;
        }
        for (const y of g[x]) {
            path[i] = y;
            dfs(i - 1, Math.floor(x / y), Math.min(mi, y), Math.max(mx, y));
        }
    };
    dfs(k - 1, n, Infinity, 0);
    return ans;
}
