"use strict";
function cherryPickup(grid) {
    const rows = grid.length, cols = grid[0].length;
    let dp = new Map([[`0,${cols - 1}`, grid[0][0] + (cols > 1 ? grid[0][cols - 1] : 0)]]);
    for (let r = 1; r < rows; r++) {
        const next = new Map();
        for (const [key, score] of dp) {
            const [a, b] = key.split(',').map(Number);
            for (let na = a - 1; na <= a + 1; na++)
                for (let nb = b - 1; nb <= b + 1; nb++) {
                    if (na < 0 || nb < 0 || na >= cols || nb >= cols)
                        continue;
                    const state = `${na},${nb}`;
                    const value = score + grid[r][na] + (na === nb ? 0 : grid[r][nb]);
                    next.set(state, Math.max(next.get(state) ?? -Infinity, value));
                }
        }
        dp = next;
    }
    return Math.max(...dp.values());
}
