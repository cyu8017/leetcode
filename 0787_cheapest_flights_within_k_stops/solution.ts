// LeetCode 0787 - Cheapest Flights Within K Stops
// https://leetcode.com/problems/cheapest-flights-within-k-stops/

export function findCheapestPrice(n: number, flights: number[][], src: number, dst: number, k: number): number {
    const INF = Math.floor(Number.MAX_SAFE_INTEGER / 4);
    let dist = new Array(n).fill(INF);
    dist[src] = 0;
    for (let i = 0; i <= k; i++) {
        const nxt = dist.slice();
        for (const [u, v, price] of flights) {
            if (dist[u] !== INF && dist[u] + price < nxt[v]) {
                nxt[v] = dist[u] + price;
            }
        }
        dist = nxt;
    }
    return dist[dst] === INF ? -1 : dist[dst];
}
