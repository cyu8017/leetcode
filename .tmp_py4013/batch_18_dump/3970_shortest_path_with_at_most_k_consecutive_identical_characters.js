// LeetCode 3970 - Shortest Path With At Most K Consecutive Identical Characters
// https://leetcode.com/problems/shortest-path-with-at-most-k-consecutive-identical-characters/

var shortestPath = function(n, edges, labels, k) {
    const graph = Array.from({length: n}, () => []);
    for (const edge of edges) graph[edge[0]].push([edge[1], edge[2]]);
    const infinity = Number.MAX_SAFE_INTEGER / 4;
    const distances = Array.from({length: n}, () => new Array(k + 1).fill(infinity));
    distances[0][1] = 0;
    const pq = [[0, 0, 1]]; // [distance, node, run]
    const cmp = (a, b) => a[0] - b[0];
    while (pq.length) {
        pq.sort(cmp);
        const cur = pq.shift();
        const distance = cur[0], node = cur[1], run = cur[2];
        if (distance !== distances[node][run]) continue;
        if (node === n - 1) return distance;
        for (const e of graph[node]) {
            const to = e[0], weight = e[1];
            let nextRun = 1;
            if (labels[node] === labels[to]) nextRun = run + 1;
            if (nextRun > k) continue;
            const nextDistance = distance + weight;
            if (nextDistance < distances[to][nextRun]) {
                distances[to][nextRun] = nextDistance;
                pq.push([nextDistance, to, nextRun]);
            }
        }
    }
    return -1;
};
