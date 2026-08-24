// LeetCode 3812 - Minimum Edge Toggles On A Tree
// https://leetcode.com/problems/minimum_edge_toggles_on_a_tree/

export function minimumFlips(n: any, edges: any, start: any, target: any): any {
    const g = Array.from({length: n}, () => []);
    for (let i = 0; i < n - 1; i++) {
        const a = edges[i][0], b = edges[i][1];
        g[a].push([b, i]);
        g[b].push([a, i]);
    }
    const ans = [];
    const dfs = (a, fa) => {
        let rev = start[a] !== target[a];
        for (const e of g[a]) {
            const b = e[0], i = e[1];
            if (b !== fa && dfs(b, a)) {
                ans.push(i);
                rev = !rev;
            }
        }
        return rev;
    };
    if (dfs(0, -1)) return [-1];
    ans.sort((a, b) => a - b);
    return ans;
}
