// LeetCode 3537 - Fill a Special Grid
// https://leetcode.com/problems/fill-a-special-grid/

export function specialGrid(n: any): any {
    const m = 1 << n;
    const ans = Array.from({length: m}, () => new Array(m).fill(0));
    let val = 0;
    function dfs(x: any, y: any, k: any): any {
        if (k === 1) {
            ans[x][y] = val++;
            return;
        }
        const h = k >> 1;
        dfs(x, y, h);
        dfs(x + h, y, h);
        dfs(x + h, y - h, h);
        dfs(x, y - h, h);
    }    dfs(0, m - 1, m);
    return ans;
}
