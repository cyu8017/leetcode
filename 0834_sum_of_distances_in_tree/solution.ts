// LeetCode 0834 - Sum of Distances in Tree
// https://leetcode.com/problems/sum-of-distances-in-tree/

export function sumOfDistancesInTree(n: number, edges: number[][]): number[] {
    const graph = Array.from({ length: n }, () => []);
    for (const [a, b] of edges) {
        graph[a].push(b);
        graph[b].push(a);
    }
    const count = new Array(n).fill(1);
    const ans = new Array(n).fill(0);
    const post = (node, parent) => {
        for (const child of graph[node]) {
            if (child === parent) continue;
            post(child, node);
            count[node] += count[child];
            ans[node] += ans[child] + count[child];
        }
    };
    const reroot = (node, parent) => {
        for (const child of graph[node]) {
            if (child === parent) continue;
            ans[child] = ans[node] - count[child] + (n - count[child]);
            reroot(child, node);
        }
    };
    post(0, -1);
    reroot(0, -1);
    return ans;
}
