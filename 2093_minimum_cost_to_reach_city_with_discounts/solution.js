// LeetCode 2093 - Minimum Cost to Reach City With Discounts
// https://leetcode.com/problems/minimum-cost-to-reach-city-with-discounts/

/**
 * @param {number} n
 * @param {number[][]} highways
 * @param {number} discounts
 * @return {number}
 */
var minimumCost = function(n, highways, discounts) {
    const g = Array.from({length: n}, () => []);
    for (const [a, b, c] of highways) {
        g[a].push([b, c]);
        g[b].push([a, c]);
    }
    const INF = 1 << 30;
    const dist = Array.from({length: n}, () => new Array(discounts + 1).fill(INF));
    const pq = [];
    const push = (item) => {
        pq.push(item);
        let i = pq.length - 1;
        while (i > 0) {
            const p = (i - 1) >> 1;
            if (pq[p][0] <= pq[i][0]) break;
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
                let l = i * 2 + 1, r = l + 1, s = i;
                if (l < pq.length && pq[l][0] < pq[s][0]) s = l;
                if (r < pq.length && pq[r][0] < pq[s][0]) s = r;
                if (s === i) break;
                [pq[s], pq[i]] = [pq[i], pq[s]];
                i = s;
            }
        }
        return top;
    };
    dist[0][discounts] = 0;
    push([0, 0, discounts]);
    while (pq.length) {
        const [cost, city, disc] = pop();
        if (city === n - 1) return cost;
        if (cost > dist[city][disc]) continue;
        for (const [v, w] of g[city]) {
            if (cost + w < dist[v][disc]) {
                dist[v][disc] = cost + w;
                push([dist[v][disc], v, disc]);
            }
            if (disc > 0 && cost + Math.floor(w / 2) < dist[v][disc - 1]) {
                dist[v][disc - 1] = cost + Math.floor(w / 2);
                push([dist[v][disc - 1], v, disc - 1]);
            }
        }
    }
    return -1;
};
