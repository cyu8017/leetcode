// LeetCode 1778 - Shortest Path in a Hidden Grid
// https://leetcode.com/problems/shortest-path-in-a-hidden-grid/

/**
 * @param {number[][]} grid
 * @return {number}
 */
var findShortestPath = function(grid) {
    const DIR = { U: [-1, 0], D: [1, 0], L: [0, -1], R: [0, 1] };
    const OPP = { U: "D", D: "U", L: "R", R: "L" };
    const m = grid.length;
    const n = grid[0].length;
    let r = 0;
    let c = 0;
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (grid[i][j] === -1) {
                r = i;
                c = j;
            }
        }
    }
    const master = {
        canMove(d) {
            const nr = r + DIR[d][0];
            const nc = c + DIR[d][1];
            return nr >= 0 && nr < m && nc >= 0 && nc < n && grid[nr][nc] !== 0;
        },
        move(d) {
            if (this.canMove(d)) {
                r += DIR[d][0];
                c += DIR[d][1];
            }
        },
        isTarget() {
            return grid[r][c] === 2;
        },
    };

    const world = new Map([["0,0", 1]]);
    let target = null;
    if (master.isTarget()) {
        return 0;
    }

    const dfs = (cr, cc) => {
        for (const d of Object.keys(DIR)) {
            if (!master.canMove(d)) {
                continue;
            }
            master.move(d);
            const nr = cr + DIR[d][0];
            const nc = cc + DIR[d][1];
            const key = `${nr},${nc}`;
            if (!world.has(key)) {
                world.set(key, master.isTarget() ? 2 : 1);
                if (master.isTarget()) {
                    target = key;
                }
                dfs(nr, nc);
            }
            master.move(OPP[d]);
        }
    };

    dfs(0, 0);
    if (target === null) {
        return -1;
    }

    const queue = [[0, 0, 0]];
    const seen = new Set(["0,0"]);
    let head = 0;
    while (head < queue.length) {
        const [cr, cc, dist] = queue[head++];
        if (`${cr},${cc}` === target) {
            return dist;
        }
        for (const [dr, dc] of Object.values(DIR)) {
            const key = `${cr + dr},${cc + dc}`;
            if (world.has(key) && !seen.has(key)) {
                seen.add(key);
                queue.push([cr + dr, cc + dc, dist + 1]);
            }
        }
    }
    return -1;
};
