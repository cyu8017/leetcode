// LeetCode 2374 - Node With Highest Edge Score
// https://leetcode.com/problems/node-with-highest-edge-score/

class Node {
    val: number;
    children: Node[];
    constructor(val?: number, children?: Node[]) {
        this.val = val ?? 0;
        this.children = children ?? [];
    }
}

export function edgeScore(edges: number[]): number {
    const n = edges.length;
    const score = Array(n).fill(0);
    for (let i = 0; i < n; i++) score[edges[i]] += i;
    let ans = 0;
    for (let i = 1; i < n; i++)
        if (score[i] > score[ans]) ans = i;
    return ans;
}
