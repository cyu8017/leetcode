// LeetCode 3967 - Finish Time of Tasks II
// https://leetcode.com/problems/finish-time-of-tasks-ii/

function Edge(to, reverse) {
    this.to = to; this.reverse = reverse;
}

function combine(minimum, maximum, count, base) {
    if (count === 0) return base;
    return 2 * maximum - minimum + base;
}

var minFinishTime = function(n, edges, baseTime) {
    const graph = Array.from({length: n}, () => []);
    for (const edge of edges) {
        const u = edge[0], v = edge[1];
        const iu = graph[u].length, iv = graph[v].length;
        graph[u].push(new Edge(v, iv));
        graph[v].push(new Edge(u, iu));
    }
    const parent = new Array(n).fill(-2);
    const parentEdge = new Array(n).fill(0);
    parent[0] = -1;
    const order = [0];
    for (let i = 0; i < order.length; i++) {
        const u = order[i];
        for (const edge of graph[u]) {
            if (parent[edge.to] === -2) {
                parent[edge.to] = u;
                parentEdge[edge.to] = edge.reverse;
                order.push(edge.to);
            }
        }
    }
    const incoming = Array.from({length: n}, (_, i) => new Array(graph[i].length).fill(0));
    for (let oi = n - 1; oi > 0; oi--) {
        const u = order[oi];
        let minimum = 2 ** 62, maximum = -1;
        let count = 0;
        for (let edgeIndex = 0; edgeIndex < incoming[u].length; edgeIndex++) {
            if (edgeIndex === parentEdge[u]) continue;
            const value = incoming[u][edgeIndex];
            minimum = Math.min(minimum, value);
            maximum = Math.max(maximum, value);
            count++;
        }
        const value = combine(minimum, maximum, count, baseTime[u]);
        const parentNode = parent[u];
        const reverseIndex = graph[u][parentEdge[u]].reverse;
        incoming[parentNode][reverseIndex] = value;
    }
    let answer = 2 ** 62;
    for (const u of order) {
        let min1 = 2 ** 62, min2 = 2 ** 62;
        let minIndex = -1;
        let max1 = -1, max2 = -1;
        let maxIndex = -1;
        for (let i = 0; i < incoming[u].length; i++) {
            const value = incoming[u][i];
            if (value < min1) {
                min2 = min1;
                min1 = value;
                minIndex = i;
            } else if (value < min2) min2 = value;
            if (value > max1) {
                max2 = max1;
                max1 = value;
                maxIndex = i;
            } else if (value > max2) max2 = value;
        }
        const rootValue = combine(min1, max1, graph[u].length, baseTime[u]);
        answer = Math.min(answer, rootValue);
        for (let i = 0; i < graph[u].length; i++) {
            const edge = graph[u][i];
            if (edge.to === parent[u]) continue;
            if (graph[u].length === 1) {
                incoming[edge.to][edge.reverse] = baseTime[u];
                continue;
            }
            let minimum = min1, maximum = max1;
            if (i === minIndex) minimum = min2;
            if (i === maxIndex) maximum = max2;
            incoming[edge.to][edge.reverse] = combine(minimum, maximum, graph[u].length - 1, baseTime[u]);
        }
    }
    return answer;
};
