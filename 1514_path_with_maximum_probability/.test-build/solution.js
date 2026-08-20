"use strict";
// LeetCode 1514 - Path with Maximum Probability
// https://leetcode.com/problems/path-with-maximum-probability/
// @ts-nocheck
function maxProbability(n, edges, succProb, start_node, end_node) {
    const graph = Array.from({ length: n }, () => []);
    for (let i = 0; i < edges.length; i++) {
        const [a, b] = edges[i];
        const p = succProb[i];
        graph[a].push([b, p]);
        graph[b].push([a, p]);
    }
    const best = Array(n).fill(0);
    best[start_node] = 1;
    const heap = [[-1, start_node]];
    const push = (item) => {
        heap.push(item);
        let i = heap.length - 1;
        while (i > 0) {
            const p = (i - 1) >> 1;
            if (heap[p][0] <= heap[i][0])
                break;
            [heap[p], heap[i]] = [heap[i], heap[p]];
            i = p;
        }
    };
    const pop = () => {
        const top = heap[0];
        const last = heap.pop();
        if (!heap.length)
            return top;
        heap[0] = last;
        let i = 0;
        while (true) {
            let l = i * 2 + 1, r = l + 1, s = i;
            if (l < heap.length && heap[l][0] < heap[s][0])
                s = l;
            if (r < heap.length && heap[r][0] < heap[s][0])
                s = r;
            if (s === i)
                break;
            [heap[s], heap[i]] = [heap[i], heap[s]];
            i = s;
        }
        return top;
    };
    while (heap.length) {
        const [neg, node] = pop();
        const probability = -neg;
        if (node === end_node)
            return probability;
        if (probability < best[node])
            continue;
        for (const [neighbor, edgeP] of graph[node]) {
            const candidate = probability * edgeP;
            if (candidate > best[neighbor]) {
                best[neighbor] = candidate;
                push([-candidate, neighbor]);
            }
        }
    }
    return 0;
}
