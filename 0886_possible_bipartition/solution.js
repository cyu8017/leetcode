// LeetCode 0886 - Possible Bipartition
// https://leetcode.com/problems/possible-bipartition/

/**
 * @param {number} n
 * @param {number[][]} dislikes
 * @return {boolean}
 */
var possibleBipartition = function(n, dislikes) {
    const graph = Array.from({ length: n + 1 }, () => []);
    for (const e of dislikes) {
        graph[e[0]].push(e[1]);
        graph[e[1]].push(e[0]);
    }
    const color = new Map();
    for (let start = 1; start <= n; start++) {
        if (color.has(start)) continue;
        const queue = [start];
        color.set(start, 0);
        while (queue.length) {
            const node = queue.shift();
            for (const nei of graph[node]) {
                if (!color.has(nei)) {
                    color.set(nei, color.get(node) ^ 1);
                    queue.push(nei);
                } else if (color.get(nei) === color.get(node)) {
                    return false;
                }
            }
        }
    }
    return true;
};
