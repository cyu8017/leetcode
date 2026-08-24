// LeetCode 3484 - Design Spreadsheet
// https://leetcode.com/problems/design-spreadsheet/

class Spreadsheet {
    /**
     * @param {number} rows
     */
    constructor(rows) {
        this.cells = new Map();
    }

    /**
     * @param {string} cell
     * @param {number} value
     * @return {void}
     */
    setCell(cell, value) {
        this.cells.set(cell, value);
    }

    /**
     * @param {string} cell
     * @return {void}
     */
    resetCell(cell) {
        this.cells.delete(cell);
    }

    /**
     * @param {string} formula
     * @return {number}
     */
    getValue(formula) {
        if (formula.length && formula[0] === "=") formula = formula.substring(1);
        let sum = 0;
        let start = 0;
        while (start < formula.length) {
            const plus = formula.indexOf("+", start);
            const p = plus < 0 ? formula.substring(start) : formula.substring(start, plus);
            let isNum = p.length && ((p[0] >= "0" && p[0] <= "9") || (p[0] === "-" && p.length > 1));
            if (isNum) {
                for (let i = 1; i < p.length; i++) {
                    if (p[i] < "0" || p[i] > "9") { isNum = false; break; }
                }
            }
            if (isNum) sum += parseInt(p, 10);
            else sum += this.cells.get(p) || 0;
            if (plus < 0) break;
            start = plus + 1;
        }
        return sum;
    }
}
