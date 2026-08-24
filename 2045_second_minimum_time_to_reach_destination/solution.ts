// LeetCode 2045 - Second Minimum Time to Reach Destination
// https://leetcode.com/problems/second-minimum-time-to-reach-destination/

export function secondMinimum(n: number, edges: number[][], time: number, change: number): number {
    const g = Array.from({length: n + 1}, () => []);
    for (const e of edges) { g[e[0]].push(e[1]); g[e[1]].push(e[0]); }
    const dist1 = new Array(n + 1).fill(-1), dist2 = new Array(n + 1).fill(-1);
    const q = [[1, 0]];
    dist1[1] = 0;
    while (q.length) {
        const [u, d] = q.shift();
        for (const v of g[u]) {
            const nd = d + 1;
            if (dist1[v] === -1) { dist1[v] = nd; q.push([v, nd]); }
            else if (dist2[v] === -1 && nd > dist1[v]) { dist2[v] = nd; q.push([v, nd]); }
        }
    }
    const steps = dist2[n];
    let ans = 0;
    for (let i = 0; i < steps; i++) {
        if (Math.floor(ans / change) % 2 === 1) ans += change - ans % change;
        ans += time;
    }
    return ans;
}
