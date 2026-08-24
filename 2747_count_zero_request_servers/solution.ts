// LeetCode 2747 - Count Zero Request Servers
// https://leetcode.com/problems/count-zero-request-servers/

export function countServers(n: number, logs: number[][], x: number, queries: number[]): number[] {
    logs.sort((a, b) => a[1] - b[1]);
    const qs = queries.map((t, i) => [t, i]).sort((a, b) => a[0] - b[0]);
    const ans = Array(queries.length);
    const cnt = new Map();
    let active = 0, l = 0, r = 0;
    for (const [t, qi] of qs) {
        while (r < logs.length && logs[r][1] <= t) {
            const id = logs[r][0];
            const c = cnt.get(id) || 0;
            if (c === 0) active++;
            cnt.set(id, c + 1);
            r++;
        }
        while (l < r && logs[l][1] < t - x) {
            const id = logs[l][0];
            const c = cnt.get(id) - 1;
            cnt.set(id, c);
            if (c === 0) active--;
            l++;
        }
        ans[qi] = n - active;
    }
    return ans;
}
