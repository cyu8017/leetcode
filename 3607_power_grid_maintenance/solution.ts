// LeetCode 3607 - Power Grid Maintenance
// https://leetcode.com/problems/power-grid-maintenance/

export function processQueries(c: any, connections: any, queries: any): any {
    const parent = new Array(c + 1);
    for (let i = 0; i <= c; i++) parent[i] = i;
    function find(x: any): any {
        if (parent[x] !== x) parent[x] = find(parent[x]);
        return parent[x];
    }    function unite(a: any, b: any): any {
        let ra = find(a), rb = find(b);
        if (ra !== rb) {
            if (ra < rb) parent[rb] = ra;
            else parent[ra] = rb;
        }
    }    for (const e of connections) unite(e[0], e[1]);
    const online = new Array(c + 1).fill(true);
    const comp = new Map();
    for (let i = 1; i <= c; i++) {
        const r = find(i);
        if (!comp.has(r)) comp.set(r, []);
        comp.get(r).push(i);
    }
    for (const ids of comp.values()) ids.sort((a, b) => a - b);
    const ptr = new Map();
    const ans = [];
    for (const q of queries) {
        const t = q[0], x = q[1];
        if (t === 2) {
            online[x] = false;
            continue;
        }
        if (online[x]) {
            ans.push(x);
            continue;
        }
        const r = find(x);
        const ids = comp.get(r);
        let p = ptr.get(r) || 0;
        while (p < ids.length && !online[ids[p]]) p++;
        ptr.set(r, p);
        ans.push(p < ids.length ? ids[p] : -1);
    }
    return ans;
}
