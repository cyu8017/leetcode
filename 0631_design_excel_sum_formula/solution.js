// LeetCode 0631 - Design Excel Sum Formula
// https://leetcode.com/problems/design-excel-sum-formula/

/**
 * @param {number} height
 * @param {character} width
 */
var Excel = function(height, width) {
    this.values = Array.from({ length: height + 1 }, () => Array(width.charCodeAt(0) - 64).fill(0));
    this.formulas = new Map();
};

Excel.prototype._key = function(row, col) {
    return (BigInt(row) << 32n) | BigInt(col >>> 0);
};

Excel.prototype._parse = function(cell) {
    return [Number(cell.substring(1)), cell.charCodeAt(0) - 65];
};

Excel.prototype._eval = function(row, col) {
    const formula = this.formulas.get(this._key(row, col).toString());
    if (formula) {
        let total = 0;
        for (const cell of formula) total += this._eval(cell[0], cell[1]);
        return total;
    }
    return this.values[row][col];
};

/**
 * @param {number} row
 * @param {character} column
 * @param {number} val
 * @return {void}
 */
Excel.prototype.set = function(row, column, val) {
    const col = column.charCodeAt(0) - 65;
    this.formulas.delete(this._key(row, col).toString());
    this.values[row][col] = val;
};

/**
 * @param {number} row
 * @param {character} column
 * @return {number}
 */
Excel.prototype.get = function(row, column) {
    return this._eval(row, column.charCodeAt(0) - 65);
};

/**
 * @param {number} row
 * @param {character} column
 * @param {string[]} numbers
 * @return {number}
 */
Excel.prototype.sum = function(row, column, numbers) {
    const col = column.charCodeAt(0) - 65;
    const cells = [];
    for (const token of numbers) {
        const colon = token.indexOf(":");
        if (colon >= 0) {
            const p1 = this._parse(token.substring(0, colon));
            const p2 = this._parse(token.substring(colon + 1));
            for (let r = p1[0]; r <= p2[0]; ++r) {
                for (let c = p1[1]; c <= p2[1]; ++c) cells.push([r, c]);
            }
        } else {
            cells.push(this._parse(token));
        }
    }
    this.formulas.set(this._key(row, col).toString(), cells);
    return this._eval(row, col);
};
