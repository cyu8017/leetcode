// LeetCode 1245 - Tree Diameter
// https://leetcode.com/problems/tree-diameter/

function treeDiameter(edges: number[][]): number {
    if (!edges.length) return 0;
    const graph = new Map();
    for (const [a, b] of edges) {
        if (!graph.has(a)) graph.set(a, []);
        if (!graph.has(b)) graph.set(b, []);
        graph.get(a).push(b);
        graph.get(b).push(a);
    }
    const farthest = (start) => {
        const queue = [[start, 0]];
        const seen = new Set([start]);
        let last = [start, 0];
        while (queue.length) {
            last = queue.shift();
            for (const v of graph.get(last[0]) || []) {
                if (!seen.has(v)) {
                    seen.add(v);
                    queue.push([v, last[1] + 1]);
                }
            }
        }
        return last;
    };
    const endpoint = farthest(edges[0][0])[0];
    return farthest(endpoint)[1];
}
