// LeetCode 0964 - Least Operators to Express Number
// https://leetcode.com/problems/least-operators-to-express-number/

export function leastOpsExpressTarget(x: number, target: number): number {
    const memo = new Map();
    const dfs = (t) => {
        if (memo.has(t)) return memo.get(t);
        if (x > t) {
            const ans = Math.min(2 * t - 1, 2 * (x - t));
            memo.set(t, ans);
            return ans;
        }
        if (x === t) {
            memo.set(t, 0);
            return 0;
        }
        let prod = x, n = 0;
        while (prod < t) {
            prod *= x;
            n++;
        }
        if (prod === t) {
            memo.set(t, n);
            return n;
        }
        let ans = dfs(t - Math.floor(prod / x)) + n;
        if (prod < 2 * t) ans = Math.min(ans, dfs(prod - t) + n + 1);
        memo.set(t, ans);
        return ans;
    };
    return dfs(target);
}
