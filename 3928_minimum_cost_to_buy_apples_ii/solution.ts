// LeetCode 3928 - Minimum Cost to Buy Apples II
// https://leetcode.com/problems/minimum-cost-to-buy-apples-ii/

export function minCostToBuyApples(n: any, prices: any, roads: any): any {
    const g = Array.from({length: n}, () => []);
    for (const road of roads) {
        const empty = road[2], full = road[2] * road[3];
        g[road[0]].push({to: road[1], empty, full});
        g[road[1]].push({to: road[0], empty, full});
    }
    const inf = 2 ** 62;
    const answer = new Array(n);
    for (let source = 0; source < n; source++) {
        const emptyDist = dijkstra(n, g, source, false, inf);
        const fullDist = dijkstra(n, g, source, true, inf);
        let best = prices[source];
        for (let shop = 0; shop < n; shop++) {
            if (emptyDist[shop] === inf || fullDist[shop] === inf) continue;
            const total = emptyDist[shop] + fullDist[shop] + prices[shop];
            if (total < best) best = total;
        }
        answer[source] = best;
    }
    return answer;
}
function dijkstra(n: any, g: any, source: any, carrying: any, inf: any): any {
    const dist = new Array(n).fill(inf);
    dist[source] = 0;
    const pq = [[0, source]];
    while (pq.length) {
        pq.sort((a, b) => a[0] - b[0]);
        const cur = pq.shift();
        const d = cur[0], node = cur[1];
        if (d !== dist[node]) continue;
        for (const e of g[node]) {
            const weight = carrying ? e.full : e.empty;
            const next = d + weight;
            if (next < dist[e.to]) {
                dist[e.to] = next;
                pq.push([next, e.to]);
            }
        }
    }
    return dist;
}
