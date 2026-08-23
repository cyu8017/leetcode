// LeetCode 1263 - Minimum Moves to Move a Box to Their Target Location
// https://leetcode.com/problems/minimum-moves-to-move-a-box-to-their-target-location/

/**
 * @param {character[][]} grid
 * @return {number}
 */
var minPushBox = function(grid) {
    const m = grid.length;
    const n = grid[0].length;
    let box = null;
    let player = null;
    let target = null;
    for (let r = 0; r < m; r++) {
        for (let c = 0; c < n; c++) {
            if (grid[r][c] === 'B') box = [r, c];
            else if (grid[r][c] === 'S') player = [r, c];
            else if (grid[r][c] === 'T') target = [r, c];
        }
    }

    const dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]];

    const reachable = (start, blocked) => {
        const seen = new Set([`${start[0]},${start[1]}`]);
        const stack = [start];
        while (stack.length) {
            const [r, c] = stack.pop();
            for (const [dr, dc] of dirs) {
                const nr = r + dr;
                const nc = c + dc;
                const key = `${nr},${nc}`;
                if (nr < 0 || nr >= m || nc < 0 || nc >= n || grid[nr][nc] === '#') continue;
                if (nr === blocked[0] && nc === blocked[1]) continue;
                if (seen.has(key)) continue;
                seen.add(key);
                stack.push([nr, nc]);
            }
        }
        return seen;
    };

    const queue = [[box[0], box[1], player[0], player[1], 0]];
    const seen = new Set([`${box[0]},${box[1]},${player[0]},${player[1]}`]);

    while (queue.length) {
        const [br, bc, pr, pc, pushes] = queue.shift();
        if (br === target[0] && bc === target[1]) return pushes;
        const canReach = reachable([pr, pc], [br, bc]);
        for (const [dr, dc] of dirs) {
            const sr = br - dr;
            const sc = bc - dc;
            const nbr = br + dr;
            const nbc = bc + dc;
            if (!canReach.has(`${sr},${sc}`)) continue;
            if (nbr < 0 || nbr >= m || nbc < 0 || nbc >= n || grid[nbr][nbc] === '#') continue;
            const state = `${nbr},${nbc},${br},${bc}`;
            if (seen.has(state)) continue;
            seen.add(state);
            queue.push([nbr, nbc, br, bc, pushes + 1]);
        }
    }
    return -1;
};
