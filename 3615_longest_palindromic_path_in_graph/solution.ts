// LeetCode 3615 - Longest Palindromic Path in Graph
// https://leetcode.com/problems/longest-palindromic-path-in-graph/

export function maxLen(n: any, edges: any, label: any): any {
    const g = Array.from({length: n}, () => []);
    for (const e of edges) {
        g[e[0]].push(e[1]);
        g[e[1]].push(e[0]);
    }
    const pack = (a, b) => (BigInt(a) << 32n) | BigInt(b >>> 0);
    const expandPal = (l, r) => {
        const vis = new Set();
        const q = [];
        const len0 = l !== r ? 2 : 1;
        q.push([l, r, len0]);
        let best = len0;
        vis.add(pack(Math.min(l, r), Math.max(l, r)).toString());
        while (q.length) {
            const cur = q.shift();
            for (const a of g[cur[0]]) {
                for (const b of g[cur[1]]) {
                    if (a === b || label[a] !== label[b]) continue;
                    const p = pack(Math.min(a, b), Math.max(a, b)).toString();
                    if (vis.has(p)) continue;
                    vis.add(p);
                    const nl = cur[2] + 2;
                    best = Math.max(best, nl);
                    q.push([a, b, nl]);
                }
            }
        }
        return best;
    };
    let ans = 1;
    for (let i = 0; i < n; i++) {
        ans = Math.max(ans, expandPal(i, i));
        for (const j of g[i]) {
            if (i < j && label[i] === label[j])
                ans = Math.max(ans, expandPal(i, j));
        }
    }
    return ans;
}
