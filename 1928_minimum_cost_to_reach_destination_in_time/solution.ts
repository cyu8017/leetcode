// LeetCode 1928 - Minimum Cost to Reach Destination in Time
// https://leetcode.com/problems/minimum-cost-to-reach-destination-in-time/

function minCost(maxTime: number, edges: number[][], passingFee: number[]): number {
    const n = passingFee.length;
    const graph: number[][][] = Array.from({ length: n }, () => []);
    for (const [u, v, t] of edges) {
        graph[u].push([v, t]);
        graph[v].push([u, t]);
    }
    const minTime = new Array(n).fill(maxTime + 1);
    const pq: number[][] = [[passingFee[0], 0, 0]];
    const push = (item: number[]): void => {
        pq.push(item);
        let i = pq.length - 1;
        while (i > 0) {
            const p = (i - 1) >> 1;
            if (pq[p][0] <= pq[i][0]) break;
            [pq[p], pq[i]] = [pq[i], pq[p]];
            i = p;
        }
    };
    const pop = (): number[] => {
        const top = pq[0];
        const last = pq.pop()!;
        if (!pq.length) return top;
        pq[0] = last;
        let i = 0;
        while (true) {
            let smallest = i;
            const l = 2 * i + 1, r = 2 * i + 2;
            if (l < pq.length && pq[l][0] < pq[smallest][0]) smallest = l;
            if (r < pq.length && pq[r][0] < pq[smallest][0]) smallest = r;
            if (smallest === i) break;
            [pq[smallest], pq[i]] = [pq[i], pq[smallest]];
            i = smallest;
        }
        return top;
    };
    while (pq.length) {
        const [cost, time, u] = pop();
        if (time >= minTime[u]) continue;
        minTime[u] = time;
        if (u === n - 1) return cost;
        for (const [v, dt] of graph[u]) {
            const nt = time + dt;
            if (nt <= maxTime && nt < minTime[v]) push([cost + passingFee[v], nt, v]);
        }
    }
    return -1;
}
