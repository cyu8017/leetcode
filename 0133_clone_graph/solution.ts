// LeetCode 0133 - Clone Graph
// https://leetcode.com/problems/clone-graph/

export class Node {
    val: number;
    neighbors: Node[];

    constructor(val = 0, neighbors: Node[] = []) {
        this.val = val;
        this.neighbors = neighbors;
    }
}

export function cloneGraph(node: Node | null): Node | null {
    if (!node) return null;

    const clones = new Map<Node, Node>();
    const dfs = (current: Node): Node => {
        const existing = clones.get(current);
        if (existing) return existing;

        const copy = new Node(current.val);
        clones.set(current, copy);
        copy.neighbors = current.neighbors.map(dfs);
        return copy;
    };

    return dfs(node);
}