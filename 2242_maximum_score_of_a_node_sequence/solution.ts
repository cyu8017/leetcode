// LeetCode 2242 - Maximum Score of a Node Sequence
// https://leetcode.com/problems/maximum-score-of-a-node-sequence/

class Node {
    val: number;
    children: Node[];
    constructor(val?: number, children?: Node[]) {
        this.val = val ?? 0;
        this.children = children ?? [];
    }
}

export function maximumScore(scores: number[], edges: number[][]): number {
    const n = scores.length;
    const top = Array.from({length: n}, () => []);
    const g = Array.from({length: n}, () => []);
    for (const e of edges) {
        g[e[0]].push(e[1]);
        g[e[1]].push(e[0]);
    }
    for (let i = 0; i < n; i++) {
        for (const v of g[i]) {
            top[i].push(v);
            for (let j = top[i].length - 1; j > 0; j--) {
                if (scores[top[i][j]] > scores[top[i][j - 1]]) {
                    const tmp = top[i][j];
                    top[i][j] = top[i][j - 1];
                    top[i][j - 1] = tmp;
                }
            }
            if (top[i].length > 3) top[i].length = 3;
        }
    }
    let ans = -1;
    for (const e of edges) {
        const a = e[0], b = e[1];
        for (const c of top[a]) {
            if (c === b) continue;
            for (const d of top[b]) {
                if (d === a || d === c) continue;
                ans = Math.max(ans, scores[a] + scores[b] + scores[c] + scores[d]);
            }
        }
    }
    return ans;
}
