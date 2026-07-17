// LeetCode 1778 - Shortest Path in a Hidden Grid
// https://leetcode.com/problems/shortest-path-in-a-hidden-grid/

function findShortestPath(grid: number[][]): number {
    const DIR: Record<string, [number, number]> = {
        U: [-1, 0],
        D: [1, 0],
        L: [0, -1],
        R: [0, 1],
    };
    const OPP: Record<string, string> = { U: "D", D: "U", L: "R", R: "L" };
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
    const canMove = (d: string): boolean => {
        const nr = r + DIR[d][0];
        const nc = c + DIR[d][1];
        return nr >= 0 && nr < m && nc >= 0 && nc < n && grid[nr][nc] !== 0;
    };
    const move = (d: string): void => {
        if (canMove(d)) {
            r += DIR[d][0];
            c += DIR[d][1];
        }
    };
    const isTarget = (): boolean => grid[r][c] === 2;

    const world = new Map<string, number>([["0,0", 1]]);
    let target: string | null = null;
    if (isTarget()) {
        return 0;
    }

    const dfs = (cr: number, cc: number): void => {
        for (const d of Object.keys(DIR)) {
            if (!canMove(d)) {
                continue;
            }
            move(d);
            const nr = cr + DIR[d][0];
            const nc = cc + DIR[d][1];
            const key = `${nr},${nc}`;
            if (!world.has(key)) {
                world.set(key, isTarget() ? 2 : 1);
                if (isTarget()) {
                    target = key;
                }
                dfs(nr, nc);
            }
            move(OPP[d]);
        }
    };

    dfs(0, 0);
    if (target === null) {
        return -1;
    }

    const queue: [number, number, number][] = [[0, 0, 0]];
    const seen = new Set<string>(["0,0"]);
    let head = 0;
    while (head < queue.length) {
        const [cr, cc, dist] = queue[head++];
        if (`${cr},${cc}` === target) {
            return dist;
        }
        for (const d of Object.keys(DIR)) {
            const key = `${cr + DIR[d][0]},${cc + DIR[d][1]}`;
            if (world.has(key) && !seen.has(key)) {
                seen.add(key);
                queue.push([cr + DIR[d][0], cc + DIR[d][1], dist + 1]);
            }
        }
    }
    return -1;
}
