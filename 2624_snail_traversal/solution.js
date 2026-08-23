// LeetCode 2624 - Snail Traversal
// https://leetcode.com/problems/snail-traversal/

Array.prototype.snail = function(rowsCount, colsCount) {
    if (rowsCount * colsCount !== this.length) return [];
    const ans = Array.from({ length: rowsCount }, () => new Array(colsCount));
    let idx = 0;
    for (let c = 0; c < colsCount; c++) {
        if (c % 2 === 0) {
            for (let r = 0; r < rowsCount; r++) ans[r][c] = this[idx++];
        } else {
            for (let r = rowsCount - 1; r >= 0; r--) ans[r][c] = this[idx++];
        }
    }
    return ans;
};
