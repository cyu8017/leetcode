export function maxKilledEnemies(grid: string[][]): number {
    if (!grid.length || !grid[0].length) return 0;
    const rows = grid.length;
    const cols = grid[0].length;
    const rowHits = Array.from({ length: rows }, () => Array(cols).fill(0));
    const colHits = Array.from({ length: rows }, () => Array(cols).fill(0));

    for (let row = 0; row < rows; row += 1) {
        let count = 0;
        for (let col = 0; col < cols; col += 1) {
            if (grid[row][col] === "W") count = 0;
            else if (grid[row][col] === "E") count += 1;
            else rowHits[row][col] = count;
        }
        count = 0;
        for (let col = cols - 1; col >= 0; col -= 1) {
            if (grid[row][col] === "W") count = 0;
            else if (grid[row][col] === "E") count += 1;
            else rowHits[row][col] += count;
        }
    }

    for (let col = 0; col < cols; col += 1) {
        let count = 0;
        for (let row = 0; row < rows; row += 1) {
            if (grid[row][col] === "W") count = 0;
            else if (grid[row][col] === "E") count += 1;
            else colHits[row][col] = count;
        }
        count = 0;
        for (let row = rows - 1; row >= 0; row -= 1) {
            if (grid[row][col] === "W") count = 0;
            else if (grid[row][col] === "E") count += 1;
            else colHits[row][col] += count;
        }
    }

    let best = 0;
    for (let row = 0; row < rows; row += 1) {
        for (let col = 0; col < cols; col += 1) {
            best = Math.max(best, rowHits[row][col] + colHits[row][col]);
        }
    }
    return best;
}
