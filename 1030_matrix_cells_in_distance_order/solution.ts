// LeetCode 1030 - Matrix Cells in Distance Order
// https://leetcode.com/problems/matrix-cells-in-distance-order/

function allCellsDistOrder(rows: number, cols: number, rCenter: number, cCenter: number): number[][] {
    const cells = [];
    for (let r = 0; r < rows; r++) {
        for (let c = 0; c < cols; c++) cells.push([r, c]);
    }
    cells.sort((a, b) =>
        Math.abs(a[0] - rCenter) + Math.abs(a[1] - cCenter) -
        (Math.abs(b[0] - rCenter) + Math.abs(b[1] - cCenter))
    );
    return cells;
}
