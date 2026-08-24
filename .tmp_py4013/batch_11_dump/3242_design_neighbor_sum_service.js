// LeetCode 3242 - Design Neighbor Sum Service
// https://leetcode.com/problems/design-neighbor-sum-service/

var NeighborSum = function(grid) {
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
};
NeighborSum.prototype.cal = function(value, k) {
    const p = this.d.get(value);
    let s = 0;
    for (let q = 0; q < 4; q++) {
        const x = p[0] + this.dirs[k][q], y = p[1] + this.dirs[k][q + 1];
        if (x >= 0 && x < this.grid.length && y >= 0 && y < this.grid[0].length) s += this.grid[x][y];
    }
    return s;
};
NeighborSum.prototype.adjacentSum = function(value) { return this.cal(value, 0); };
NeighborSum.prototype.diagonalSum = function(value) { return this.cal(value, 1); };
