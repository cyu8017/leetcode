// LeetCode 0882 - Reachable Nodes In Subdivided Graph
// https://leetcode.com/problems/reachable-nodes-in-subdivided-graph/

/**
 * @param {number[][]} edges
 * @param {number} maxMoves
 * @param {number} n
 * @return {number}
 */
var reachableNodes = function(edges, maxMoves, n) {
    const graph = Array.from({ length: n }, () => new Map());
    for (const e of edges) {
        graph[e[0]].set(e[1], e[2]);
        graph[e[1]].set(e[0], e[2]);
    }
    const pq = [[maxMoves, 0]];
    const push = (item) => {
        pq.push(item);
        let i = pq.length - 1;
        while (i > 0) {
            const p = (i - 1) >> 1;
            if (pq[p][0] >= pq[i][0]) break;
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
                let l = i * 2 + 1, r = l + 1, best = i;
                if (l < pq.length && pq[l][0] > pq[best][0]) best = l;
                if (r < pq.length && pq[r][0] > pq[best][0]) best = r;
                if (best === i) break;
                [pq[best], pq[i]] = [pq[i], pq[best]];
                i = best;
            }
        }
        return top;
    };
    const seen = new Map();
    while (pq.length) {
        const [moves, node] = pop();
        if (seen.has(node)) continue;
        seen.set(node, moves);
        for (const [nei, dist] of graph[node]) {
            const remain = moves - dist - 1;
            if (!seen.has(nei) && remain >= 0) push([remain, nei]);
        }
    }
    let ans = seen.size;
    for (const e of edges) {
        const left = seen.get(e[0]) || 0;
        const right = seen.get(e[1]) || 0;
        ans += Math.min(e[2], left + right);
    }
    return ans;
};
