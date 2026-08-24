// LeetCode 2662 - Minimum Cost of a Path With Special Roads
// https://leetcode.com/problems/minimum-cost-of-a-path-with-special-roads/

export function minimumCost(start: any, target: any, specialRoads: any): any {
    const points = [start, target];
    for (const r of specialRoads) {
        points.push([r[0], r[1]]);
        points.push([r[2], r[3]]);
    }
    const N = points.length;
    const man = (a, b) => Math.abs(a[0] - b[0]) + Math.abs(a[1] - b[1]);
    const g = Array.from({ length: N }, () => []);
    for (let i = 0; i < N; i++)
        for (let j = 0; j < N; j++)
            if (i !== j) g[i].push([j, man(points[i], points[j])]);
    for (const r of specialRoads) {
        let u = -1, v = -1;
        for (let i = 0; i < N; i++) {
            const p = points[i];
            if (p[0] === r[0] && p[1] === r[1]) u = i;
            if (p[0] === r[2] && p[1] === r[3]) v = i;
        }
        if (u >= 0 && v >= 0) g[u].push([v, r[4]]);
    }
    const dist = new Array(N).fill(Number.MAX_SAFE_INTEGER / 4);
    dist[0] = 0;
    const pq = [[0, 0]];
    const push = (u, d) => {
        pq.push([u, d]);
        let i = pq.length - 1;
        while (i > 0) {
            const p = (i - 1) >> 1;
            if (pq[p][1] <= pq[i][1]) break;
            [pq[p], pq[i]] = [pq[i], pq[p]];
            i = p;
        }
    };
    const pop = () => {
        const top = pq[0];
        const last = pq.pop();
        if (pq.length) {
            pq[0] = last;
            let i = 0;
            while (true) {
                let s = i, l = i * 2 + 1, r = l + 1;
                if (l < pq.length && pq[l][1] < pq[s][1]) s = l;
                if (r < pq.length && pq[r][1] < pq[s][1]) s = r;
                if (s === i) break;
                [pq[s], pq[i]] = [pq[i], pq[s]];
                i = s;
            }
        }
        return top;
    };
    while (pq.length) {
        const [id, cost] = pop();
        if (cost > dist[id]) continue;
        for (const [to, w] of g[id]) {
            if (cost + w < dist[to]) {
                dist[to] = cost + w;
                push(to, dist[to]);
            }
        }
    }
    return dist[1];
}
