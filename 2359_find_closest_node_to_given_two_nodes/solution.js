// LeetCode 2359 - Find Closest Node to Given Two Nodes
// https://leetcode.com/problems/find-closest-node-to-given-two-nodes/

/**
 * @param {number[]} edges
 * @param {number} node1
 * @param {number} node2
 * @return {number}
 */
var closestMeetingNode = function(edges, node1, node2) {
    const n = edges.length;
    const Dist = (start) => {
        const d = Array(n).fill(-1);
        let cur = start, step = 0;
        while (cur !== -1 && d[cur] === -1) {
            d[cur] = step;
            cur = edges[cur];
            step++;
        }
        return d;
    };
    const d1 = Dist(node1), d2 = Dist(node2);
    let ans = -1, best = Infinity;
    for (let i = 0; i < n; i++) {
        if (d1[i] === -1 || d2[i] === -1) continue;
        const mx = Math.max(d1[i], d2[i]);
        if (mx < best) { best = mx; ans = i; }
    }
    return ans;
};
