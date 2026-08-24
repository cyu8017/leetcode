// LeetCode 0883 - Projection Area of 3D Shapes
// https://leetcode.com/problems/projection-area-of-3d-shapes/

export function projectionArea(grid: number[][]): number {
    const n = grid.length;
    let top = 0, front = 0, side = 0;
    for (let i = 0; i < n; i++) {
        let rowMax = 0, colMax = 0;
        for (let j = 0; j < n; j++) {
            if (grid[i][j] !== 0) top++;
            rowMax = Math.max(rowMax, grid[i][j]);
            colMax = Math.max(colMax, grid[j][i]);
        }
        front += rowMax;
        side += colMax;
    }
    return top + front + side;
}
