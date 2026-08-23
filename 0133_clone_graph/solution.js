// LeetCode 0133 - Clone Graph
// https://leetcode.com/problems/clone-graph/

function Node(val = 0, neighbors = []) {
    this.val = val;
    this.neighbors = neighbors;
}

/**
 * @param {Node|null} node
 * @return {Node|null}
 */
var cloneGraph = function(node) {
    if (!node) return null;

    const clones = new Map();
    const dfs = (current) => {
        if (clones.has(current)) return clones.get(current);

        const copy = new Node(current.val);
        clones.set(current, copy);
        copy.neighbors = current.neighbors.map(dfs);
        return copy;
    };

    return dfs(node);
};