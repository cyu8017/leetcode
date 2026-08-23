// LeetCode 0675 - Cut Off Trees for Golf Event
// https://leetcode.com/problems/cut-off-trees-for-golf-event/

/**
 * @param {number[][]} forest
 * @return {number}
 */
var cutOffTree = function(forest) {
    const trees = [];
    for (let i = 0; i < forest.length; ++i) {
        for (let j = 0; j < forest[0].length; ++j) {
            if (forest[i][j] > 1) trees.push([forest[i][j], i, j]);
        }
    }
    trees.sort((a, b) => a[0] - b[0]);
    const bfs = (sr, sc, tr, tc) => {
        if (sr === tr && sc === tc) return 0;
        const m = forest.length, n = forest[0].length;
        const seen = Array.from({ length: m }, () => Array(n).fill(false));
        const queue = [[sr, sc, 0]];
        seen[sr][sc] = true;
        const dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]];
        while (queue.length) {
            const [r, c, dist] = queue.shift();
            for (const [dr, dc] of dirs) {
                const nr = r + dr, nc = c + dc;
                if (nr < 0 || nr >= m || nc < 0 || nc >= n || seen[nr][nc] || forest[nr][nc] === 0) continue;
                if (nr === tr && nc === tc) return dist + 1;
                seen[nr][nc] = true;
                queue.push([nr, nc, dist + 1]);
            }
        }
        return -1;
    };
    let sr = 0, sc = 0, steps = 0;
    for (const tree of trees) {
        const dist = bfs(sr, sc, tree[1], tree[2]);
        if (dist < 0) return -1;
        steps += dist;
        sr = tree[1];
        sc = tree[2];
    }
    return steps;
};
