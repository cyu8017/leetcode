// LeetCode 3242 - Design Neighbor Sum Service
// https://leetcode.com/problems/design-neighbor-sum-service/

export class NeighborSum {
    constructor(grid: any) {
    this.grid = grid;
    this.d = new Map();
    this.dirs = [
        [-1, 0, 1, 0, -1],
        [-1, 1, 1, -1, -1]
    ];
    for (let i = 0; i < grid.length; i++) {
        for (let j = 0; j < grid[i].length; j++) {
            this.d.set(grid[i][j], [i, j]);
        }
    }
}
    cal(value: any, k: any): any {
    const p = this.d.get(value);
    let s = 0;
    for (let q = 0; q < 4; q++) {
        const x = p[0] + this.dirs[k][q], y = p[1] + this.dirs[k][q + 1];
        if (x >= 0 && x < this.grid.length && y >= 0 && y < this.grid[0].length) s += this.grid[x][y];
    }
    return s;
}
    adjacentSum(value: any): any { return this.cal(value, 0); }
    diagonalSum(value: any): any { return this.cal(value, 1); }
}
